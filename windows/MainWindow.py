from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QPushButton, QWidget, QHBoxLayout, QLabel, QSizePolicy

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
		item = QListWidgetItem()
		item.setData(Qt.UserRole, chatThread.id)

		label = QLabel(chatThread.metadata.get('title', 'Untitled'))
		label.setObjectName('title')
		label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		label.setMinimumWidth(100)

		deleteButton = QPushButton('X')
		deleteButton.setObjectName('deleteButton')
		deleteButton.setFixedSize(16, 16)
		deleteButton.clicked.connect(lambda: self.deleteChatThread(item))

		itemWidget = QWidget()
		itemLayout = QHBoxLayout(itemWidget)
		itemLayout.setContentsMargins(0, 0, 0, 0)
		itemLayout.addWidget(label, stretch = 1, alignment = Qt.AlignLeft | Qt.AlignVCenter)
		itemLayout.addWidget(deleteButton, stretch = 0, alignment = Qt.AlignRight | Qt.AlignVCenter)

		self.ui.chatThreadsList.addItem(item)
		self.ui.chatThreadsList.setItemWidget(item, itemWidget)



	def loadChatThreadList(self):
		""" Load chat threads and populate the sidebar """
		for chatThread in self.chatClient.chatThreadList:
			self.addChatThreadToList(chatThread)
		self.currentChatThreadId = self.chatClient.chatThreadList[0].id


	@Slot()
	def createNewChat(self):
		self.chatClient.createNewChat('New Chat')


	@Slot()
	def chatThreadChanged(self, current: QListWidgetItem, previous: QListWidgetItem):
		self.selectChatThread(current.data(Qt.UserRole))


	def selectChatThread(self, chatThreadId):
		self.currentChatThreadId = chatThreadId
		self.ui.chatArea.clear()
		messages = self.chatClient.retrieveMessages(self.currentChatThreadId, 10)
		for message in messages:
			self.appendMessage(message.content[0].text.value)


	@Slot()
	def deleteChatThread(self, item: QListWidgetItem):
		self.chatClient.deleteChatThread(item.data(Qt.UserRole))


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
