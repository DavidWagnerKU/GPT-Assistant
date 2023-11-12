from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from core.GPTClient import GPTClient
from ui.ui_MainWindow import Ui_MainWindow



class MainWindow(QMainWindow):

	def __init__(self, chatClient: GPTClient):
		super(MainWindow, self).__init__()
		self.chatClient = chatClient
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.chatClient.threadAdded.connect(self.addThreadToList)

		self.loadThreadList()


	def addThreadToList(self, thread):
		item = QListWidgetItem(thread.metadata.get("title", "Untitled"))
		item.setData(Qt.UserRole, thread.id)
		self.ui.sidebar.addItem(item)


	def loadThreadList(self):
		""" Load chat threads and populate the sidebar """
		for thread in self.chatClient.threadList:
			self.addThreadToList(thread)


	@Slot()
	def createNewChat(self):
		self.chatClient.createNewChat("New Chat")


	@Slot()
	def sendMessage(self):
		self.chatClient.sendMessage(self.ui.messageTextBox.text())