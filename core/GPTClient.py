from pathlib import Path

from PySide6.QtCore import QObject, Signal
from openai import OpenAI


class GPTClient(QObject):
	messageReceived = Signal(str)
	threadAdded = Signal(object)


	def __init__(self, model, chatsDirectory: Path, systemDirectory: Path):
		super().__init__()
		self.chatsDirectory = chatsDirectory
		self.systemDirectory = systemDirectory
		self.chatsDirectory.mkdir(exist_ok=True)
		self.systemDirectory.mkdir(exist_ok=True)

		self.modelName = model
		self.threadList = []
		self.mainAssistant = None

		self.client = OpenAI()
		self.getAssistants()
		self.loadThreadList()


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


	def loadThreadList(self):
		"""
		Gets the list of threads stored in the local data directory,
		retrieving information from the API if necessary.
		"""
		self.threadList.clear()
		for filePath in self.chatsDirectory.iterdir():
			if filePath.is_file() and filePath.suffix == '.txt':
				try:
					thread = self.client.beta.threads.retrieve(filePath.stem)
					self.threadList.append(thread)
				except Exception as e:
					print(f'Error retrieving thread {filePath.stem}: {str(e)}')


	def createNewChat(self, title):
		"""
		Starts a new chat thread with the given title.
		:emits: threadAdded
		"""
		thread = self.client.beta.threads.create(metadata = {'title': title})
		self.threadList.append(thread)
		with open(self.chatsDirectory / f'{thread.id}.txt', 'w') as file:
			file.write('')
		self.threadAdded.emit(thread)


	def sendMessage(self, threadId, message):
		"""
		Sends the given user message.
		:param threadId: ID of the chat thread with which this message is associated.
		:param message: Message text to send
		:emits: messageReceived
		"""
		run = self.client.beta.threads.runs.create(
			thread_id = threadId,
			assistant_id = self.mainAssistant.id
		)
		#self.messageReceived.emit(response.choices[0].message.content)
