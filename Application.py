import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine


def handleQmlWarnings(warning):
	print("QML Warning or Error:", warning)


app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.warnings.connect(handleQmlWarnings)
engine.load('ui\\MainWindow.qml')

# Check if the engine loaded the QML file successfully
if not engine.rootObjects():
	sys.exit(-1)

sys.exit(app.exec())