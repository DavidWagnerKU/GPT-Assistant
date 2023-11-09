import os
from openai import OpenAI
from PySide6.QtCore import QObject, Slot, Signal


class GPTClient(QObject):
	messageReceived = Signal(str)

	def __init__(self, model):
		super().__init__()
		key = os.getenv("OPENAI_API_KEY")
		if not key:
			raise ValueError("The OPENAI_API_KEY environment variable is not set.")
		self.modelName = model
		self.client = OpenAI(api_key = key)

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
		self.messageReceived.emit(message)
		self.messageReceived.emit(response.choices[0].message.content)