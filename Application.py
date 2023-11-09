import sys
import argparse
from omegaconf import OmegaConf
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from GPTClient import GPTClient


def handleQmlWarnings(warning):
	print("QML Warning or Error:", warning)


parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.yaml')

cliArgs = parser.parse_args()
config = OmegaConf.load(cliArgs.config)

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

engine.warnings.connect(handleQmlWarnings)

chatClient = GPTClient(config.model)
engine.rootContext().setContextProperty("chatClient", chatClient)

engine.load("ui\\MainWindow.qml")

# Check if the engine loaded the QML file successfully
if not engine.rootObjects():
	sys.exit(-1)


sys.exit(app.exec())