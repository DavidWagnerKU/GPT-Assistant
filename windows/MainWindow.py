from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from core.GPTClient import GPTClient
from ui.ui_MainWindow import Ui_MainWindow



class MainWindow(QMainWindow):

	def __init__(self, chatClient: GPTClient):
		super(MainWindow, self).__init__()
		self.chatClient = chatClient
		self.currentChatThreadId = None

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		with open('ui\\MainWindow.css', 'r', encoding='utf-8') as file:
			self.setStyleSheet(file.read())

		self.chatClient.chatThreadAdded.connect(self.addChatThreadToList)
		self.chatClient.messageReceived.connect(self.appendMessage)

		self.loadChatThreadList()


	def addChatThreadToList(self, chatThread):
		item = QListWidgetItem(chatThread.metadata.get('title', 'Untitled'))
		item.setData(Qt.UserRole, chatThread.id)
		self.ui.chatThreadsList.addItem(item)


	def loadChatThreadList(self):
		""" Load chat threads and populate the sidebar """
		for chatThread in self.chatClient.chatThreadList:
			self.addChatThreadToList(chatThread)
		self.currentChatThreadId = self.chatClient.chatThreadList[0].id


	@Slot()
	def chatThreadChanged(self, current: QListWidgetItem, previous: QListWidgetItem):
		self.currentChatThreadId = current.data(Qt.UserRole)


	@Slot()
	def createNewChat(self):
		self.chatClient.createNewChat('New Chat')


	@Slot()
	def sendMessage(self):
		trimmedMessage = self.ui.messageTextBox.text()
		if trimmedMessage != '':
			self.appendMessage('You: ' + trimmedMessage)
			self.chatClient.sendMessage(self.currentChatThreadId, trimmedMessage)
			self.ui.messageTextBox.clear()


	@Slot(str)
	def appendMessage(self, messageText):
		"""
		Appends the given message text to the chat window
		"""
		#TODO: Accept object/dict that contains role ('user', 'AI')
		self.ui.chatArea.append('\n' + messageText)
