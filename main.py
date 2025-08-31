# Arquivo: main.py

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela_principal = MainWindow()
    janela_principal.show()
    sys.exit(app.exec())