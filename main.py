import sys
import argparse
from pathlib import Path

from omegaconf import OmegaConf
from PySide6.QtWidgets import QApplication

from core.GPTClient import GPTClient
from windows.MainWindow import MainWindow



parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.yaml')

cliArgs = parser.parse_args()
config = OmegaConf.load(cliArgs.config)

app = QApplication(sys.argv)

chatClient = GPTClient(config.model, Path('data/chats'), Path('data/system'))

window = MainWindow(chatClient)
window.show()

sys.exit(app.exec())