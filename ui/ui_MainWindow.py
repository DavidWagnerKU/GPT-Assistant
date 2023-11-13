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
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.messageLayout = QHBoxLayout()
        self.messageLayout.setObjectName(u"messageLayout")
        self.messageTextBox = QLineEdit(self.centralwidget)
        self.messageTextBox.setObjectName(u"messageTextBox")

        self.messageLayout.addWidget(self.messageTextBox)

        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")

        self.messageLayout.addWidget(self.sendButton)


        self.gridLayout.addLayout(self.messageLayout, 2, 2, 1, 1)

        self.chatArea = QTextEdit(self.centralwidget)
        self.chatArea.setObjectName(u"chatArea")
        self.chatArea.setReadOnly(True)

        self.gridLayout.addWidget(self.chatArea, 1, 2, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.newChatButton = QPushButton(self.frame)
        self.newChatButton.setObjectName(u"newChatButton")

        self.verticalLayout_3.addWidget(self.newChatButton)

        self.sidebar = QListWidget(self.frame)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.sidebar)


        self.gridLayout.addWidget(self.frame, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.newChatButton.clicked.connect(MainWindow.createNewChat)
        self.sendButton.clicked.connect(MainWindow.sendMessage)
        self.messageTextBox.returnPressed.connect(MainWindow.sendMessage)
        self.sidebar.currentItemChanged.connect(MainWindow.chatThreadChanged)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GPT Assistant", None))
        self.messageTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your message here...", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.newChatButton.setText(QCoreApplication.translate("MainWindow", u"New Chat", None))
    # retranslateUi

