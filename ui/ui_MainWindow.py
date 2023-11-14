# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QSize(250, 16777215))
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.newChatButton = QPushButton(self.sidebar)
        self.newChatButton.setObjectName(u"newChatButton")

        self.verticalLayout_3.addWidget(self.newChatButton)

        self.chatThreadsList = QListWidget(self.sidebar)
        self.chatThreadsList.setObjectName(u"chatThreadsList")

        self.verticalLayout_3.addWidget(self.chatThreadsList)


        self.horizontalLayout.addWidget(self.sidebar)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chatArea = QTextEdit(self.mainFrame)
        self.chatArea.setObjectName(u"chatArea")
        self.chatArea.setReadOnly(True)

        self.gridLayout_2.addWidget(self.chatArea, 0, 0, 1, 2)

        self.messageLayout = QHBoxLayout()
        self.messageLayout.setObjectName(u"messageLayout")
        self.messageTextBox = QLineEdit(self.mainFrame)
        self.messageTextBox.setObjectName(u"messageTextBox")

        self.messageLayout.addWidget(self.messageTextBox)

        self.sendButton = QPushButton(self.mainFrame)
        self.sendButton.setObjectName(u"sendButton")

        self.messageLayout.addWidget(self.sendButton)


        self.gridLayout_2.addLayout(self.messageLayout, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.newChatButton.clicked.connect(MainWindow.createNewChat)
        self.sendButton.clicked.connect(MainWindow.sendMessage)
        self.messageTextBox.returnPressed.connect(MainWindow.sendMessage)
        self.chatThreadsList.currentItemChanged.connect(MainWindow.chatThreadChanged)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI Assistant", None))
        self.newChatButton.setText(QCoreApplication.translate("MainWindow", u"New Chat", None))
        self.messageTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your message here...", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

