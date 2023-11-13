import time
from pathlib import Path

from PySide6.QtCore import QObject, Signal
from openai import OpenAI


class GPTClient(QObject):
	messageReceived = Signal(str)
	chatThreadAdded = Signal(object)


	def __init__(self, model, chatsDirectory: Path, systemDirectory: Path):
		super().__init__()
		self.chatsDirectory = chatsDirectory
		self.systemDirectory = systemDirectory
		self.chatsDirectory.mkdir(exist_ok=True)
		self.systemDirectory.mkdir(exist_ok=True)

		self.modelName = model
		self.chatThreadList = []
		self.mainAssistant = None

		self.client = OpenAI()
		self.getAssistants()
		self.loadChatThreadList()


	def getAssistants(self):
		"""
		Retrieve the assistants
		"""
		for filePath in self.systemDirectory.iterdir():
			if filePath.is_file() and filePath.name.startswith('asst') and filePath.suffix == '.txt':
				try:
					self.mainAssistant = self.client.beta.assistants.retrieve(filePath.stem)
					# TODO: Handle other assistants
				except Exception as e:
					print(f'Error retrieving assistant {filePath.stem}: {str(e)}')


	def loadChatThreadList(self):
		"""
		Gets the list of chat threads stored in the local data directory,
		retrieving information from the API if necessary.
		"""
		self.chatThreadList.clear()
		for filePath in self.chatsDirectory.iterdir():
			if filePath.is_file() and filePath.suffix == '.txt':
				try:
					thread = self.client.beta.threads.retrieve(filePath.stem)
					self.chatThreadList.append(thread)
				except Exception as e:
					print(f'Error retrieving chat thread {filePath.stem}: {str(e)}')
		# TODO: Sort by date, first is most recent


	def createNewChat(self, title):
		"""
		Starts a new chat thread with the given title.
		:emits: chatThreadAdded
		"""
		thread = self.client.beta.threads.create(metadata = {'title': title})
		self.chatThreadList.append(thread)
		with open(self.chatsDirectory / f'{thread.id}.txt', 'w') as file:
			file.write('')
		self.chatThreadAdded.emit(thread)


	def sendMessage(self, chatThreadId, messageText):
		"""
		Sends the given user message.
		:param chatThreadId: ID of the chat thread with which this message is associated.
		:param messageText: Message text to send
		:emits: messageReceived
		"""
		message = self.client.beta.threads.messages.create(chatThreadId, role = 'user', content = messageText)
		# TODO: Log message
		run = self.client.beta.threads.runs.create(
			thread_id = chatThreadId,
			assistant_id = self.mainAssistant.id
		)
		while run.status != 'completed':
			time.sleep(1)
			run = self.client.beta.threads.runs.retrieve(
				thread_id = chatThreadId,
				run_id = run.id
			)
		messages = self.client.beta.threads.messages.list(chatThreadId)
		self.messageReceived.emit(messages.data[0].content[0].text.value)
