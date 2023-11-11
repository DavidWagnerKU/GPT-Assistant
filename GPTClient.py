from openai import OpenAI
from PySide6.QtCore import QObject, Slot, Signal


class GPTClient(QObject):
	messageReceived = Signal(str)

	def __init__(self, model):
		super().__init__()
		self.modelName = model
		self.client = OpenAI()

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