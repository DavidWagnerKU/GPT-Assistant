from PySide6.QtCore import QObject, Signal
from openai import OpenAI


class GPTClient(QObject):
	messageReceived = Signal(str)
	threadAdded = Signal(object)


	def __init__(self, model, chatsDirectory, systemDirectory):
		super().__init__()
		self.chatsDirectory = chatsDirectory
		self.systemDirectory = systemDirectory
		self.chatsDirectory.mkdir(exist_ok=True)
		self.systemDirectory.mkdir(exist_ok=True)

		self.modelName = model
		self.threadList = []

		self.client = OpenAI()
		self.loadThreadList()


	def loadThreadList(self):
		"""
		Loads the list of threads stored in the local data directory,
		retrieving information from the API if necessary.
		"""
		self.threadList.clear()
		for filePath in self.chatsDirectory.iterdir():
			if filePath.is_file() and filePath.suffix == '.txt':
				try:
					thread = self.client.beta.threads.retrieve(filePath.stem)
					self.threadList.append(thread)
				except Exception as e:
					print(f"Error retrieving thread {filePath.stem}: {str(e)}")


	def createNewChat(self, title):
		"""
		Starts a new chat thread with the given title.
		Emits the 'threadAdded' signal.
		:return:
		"""
		thread = self.client.beta.threads.create(metadata = {'title': title})
		self.threadList.append(thread)
		with open(self.chatsDirectory / f"{thread.id}.txt", 'w') as file:
			file.write("")
		self.threadAdded.emit(thread)


	def sendMessage(self, message):
		response = self.client.chat.completions.create(
			messages = [
				{
					"role": "user",
					"content": message,
				}
			],
			model = self.modelName
		)
		self.messageReceived.emit(response.choices[0].message.content)
