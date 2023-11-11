from pathlib import Path

from PySide6.QtCore import QObject, Slot, Signal, Property
from openai import OpenAI


class GPTClient(QObject):
	chatsDirectory = Path('./data/chats')
	messageReceived = Signal(str)
	threadListChanged = Signal()

	def __init__(self, model):
		super().__init__()
		self.modelName = model
		self._threadList = []
		self.chatsDirectory.mkdir(exist_ok=True)
		self.client = OpenAI()
		self.getThreadList()

	def getThreadList(self):
		"""
		Gets the list of threads stored in the local data directory
		"""
		self._threadList.clear()
		for filePath in self.chatsDirectory.iterdir():
			if filePath.is_file() and filePath.suffix == '.txt':
				try:
					threadInfo = self.client.beta.threads.retrieve(filePath.stem)
					self._threadList.append(threadDictFromInfo(threadInfo))
				except Exception as e:
					print(f"Error retrieving thread {filePath.stem}: {str(e)}")


	@Property(list, notify=threadListChanged)
	def threadList(self):
		return self._threadList

	@threadList.setter
	def threadList(self, value):
		if self._threadList == value:
			return
		self._threadList = value
		self.threadListChanged.emit()


	@Slot(str)
	def createNewChat(self, title):
		threadInfo = self.client.beta.threads.create(metadata = {'title': title})
		self._threadList.append(threadDictFromInfo(threadInfo))
		with open(self.chatsDirectory / f"{threadInfo.id}.txt", 'w') as file:
			file.write("")



	@Slot(str)
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


def threadDictFromInfo(threadInfo):
	"""
	:param threadInfo: An OpenAI `Thread` object
	:return: A dict representing the given thread
	"""
	return {
		'id': threadInfo.id,
		'timeCreated': threadInfo.created_at,
		'title': threadInfo.metadata.get('title', 'Untitled')
	}