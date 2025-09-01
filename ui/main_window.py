# Arquivo: ui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QLabel, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os

from core.data_analyzer import AnalisadorDados
from ui.data_window import DataWindow

# Janela principal da aplicação, responsável pela interface do usuário e controle do fluxo.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Instância do Analisador de Dados
        self.analisador = AnalisadorDados()
        
        # Carrega os dados do arquivo ao iniciar a aplicação.
        caminho_dados = os.path.join('data', 'DadosCovidSergipe.txt')
        self.analisador.carregar_dados(caminho_dados)
        
        # 2. Configuração da janela principal
        self.setWindowTitle("PROJETOPOO-PYTHON")
        self.setFixedSize(800, 600)
        
        # 3. Criação dos widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Aplica estilos CSS para personalizar a aparência da interface.
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000;
            }
            QLabel {
                background-color: transparent;
                color: white;
            }
            QComboBox {
                background-color: #333;
                color: white;
                font-size: 18px;
                padding: 10px 15px;
                border-radius: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #333;
                color: white;
            }
            QPushButton {
                background-color: #555;
                color: white;
                font-size: 18px;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
            }
            QFrame {
                background-color: #333;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.layout_principal = QVBoxLayout(self.central_widget)
        
        # Frame para exibir o mapa.
        self.frame_mapa = QFrame(self.central_widget)
        self.layout_mapa = QVBoxLayout(self.frame_mapa)
        self.layout_principal.addWidget(self.frame_mapa, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Carrega e exibe a imagem do mapa.
        self.mapa_label = QLabel()
        self.mapa_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        caminho_mapa = os.path.join('assets', 'mapa_sergipe.jpg')
        if os.path.exists(caminho_mapa):
            pixmap_mapa = QPixmap(caminho_mapa)
            self.mapa_label.setPixmap(pixmap_mapa.scaled(600, 500, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.mapa_label.setText("Mapa de Sergipe não encontrado na pasta 'assets'.")
        
        self.layout_mapa.addWidget(self.mapa_label)
        
        # Layout para os controles do usuário (ComboBox e botão Sair).
        self.layout_botoes = QHBoxLayout()
        self.layout_botoes.addStretch()
        
        # ComboBox populada com a lista de municípios.
        self.buscar_cidade_combo = QComboBox()
        self.buscar_cidade_combo.setPlaceholderText("Selecione uma cidade")
        self.buscar_cidade_combo.addItems(self.analisador.obter_lista_municipios())
        self.buscar_cidade_combo.setEditable(False)
        self.buscar_cidade_combo.setFixedWidth(450)
        self.layout_botoes.addWidget(self.buscar_cidade_combo)
        
        # Botão para fechar a aplicação.
        self.sair_button = QPushButton("Sair")
        self.sair_button.setFixedWidth(100)
        self.layout_botoes.addWidget(self.sair_button)
        
        self.layout_botoes.addStretch()
        
        self.layout_principal.addLayout(self.layout_botoes)
        self.layout_principal.addStretch()
        
        # Referência para a janela de dados, inicializada como None.
        self.data_window = None

        # 4. Conecta os eventos dos widgets aos métodos correspondentes.
        self.buscar_cidade_combo.currentIndexChanged.connect(self.abrir_janela_dados)
        self.sair_button.clicked.connect(self.mostrar_aviso_saida)

    # Método para exibir um aviso de confirmação antes de sair.
    def mostrar_aviso_saida(self):
        aviso = QMessageBox()
        aviso.setWindowTitle("Aviso")
        aviso.setText("Você tem certeza que deseja sair?")
        aviso.setIcon(QMessageBox.Icon.Question)
        aviso.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        aviso.setDefaultButton(QMessageBox.StandardButton.No)

        aviso.setStyleSheet("background-color: #333; color: white;")

        resposta = aviso.exec()

        if resposta == QMessageBox.StandardButton.Yes:
            self.close()
            
    # Método para abrir a janela de dados do município selecionado.
    def abrir_janela_dados(self):
        nome_cidade = self.buscar_cidade_combo.currentText()
        if nome_cidade:
            dados = self.analisador.obter_dados_completos(nome_cidade)
            
            if dados:
                self.data_window = DataWindow(nome_cidade, dados)
                self.data_window.show()
            else:
                print("Dados não encontrados para a cidade selecionada.")