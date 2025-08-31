# Arquivo: ui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QLabel, QComboBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os

from core.data_analyzer import AnalisadorDados

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Instância do Analisador de Dados
        self.analisador = AnalisadorDados()
        
        # Carrega os dados na inicialização
        # O caminho do arquivo é relativo à pasta do projeto
        caminho_dados = os.path.join('data', 'DadosCovidSergipe.txt')
        self.analisador.carregar_dados(caminho_dados)
        
        # 2. Configuração da janela principal
        self.setWindowTitle("PROJETOPOO-PYTHON")
        self.setFixedSize(800, 600)
        
        # 3. Criação dos widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout_principal = QVBoxLayout(self.central_widget)
        
        # Imagem do mapa de Sergipe
        self.mapa_label = QLabel()
        self.mapa_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        caminho_mapa = os.path.join('assets', 'mapa_sergipe.jpg')
        if os.path.exists(caminho_mapa):
            pixmap_mapa = QPixmap(caminho_mapa)
            self.mapa_label.setPixmap(pixmap_mapa.scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.mapa_label.setText("Mapa de Sergipe não encontrado na pasta 'assets'.")
        
        # ComboBox para a lista de cidades
        self.buscar_cidade_combo = QComboBox()
        self.buscar_cidade_combo.setPlaceholderText("Selecione uma cidade")
        self.buscar_cidade_combo.addItems(self.analisador.obter_lista_municipios())
        self.buscar_cidade_combo.setEditable(False)
        
        # Rótulos para exibir os dados
        self.municipio_label = QLabel("Município: ")
        self.mortes_label = QLabel("Mortes: ")
        self.casos_label = QLabel("Casos: ")
        self.letalidade_label = QLabel("Letalidade: ")
        
        # 4. Adiciona os widgets aos layouts
        self.layout_principal.addWidget(self.mapa_label)
        
        layout_combobox = QHBoxLayout()
        layout_combobox.addStretch()
        layout_combobox.addWidget(self.buscar_cidade_combo)
        layout_combobox.addStretch()
        self.layout_principal.addLayout(layout_combobox)
        
        layout_dados = QVBoxLayout()
        layout_dados.addWidget(self.municipio_label)
        layout_dados.addWidget(self.mortes_label)
        layout_dados.addWidget(self.casos_label)
        layout_dados.addWidget(self.letalidade_label)
        self.layout_principal.addLayout(layout_dados)
        
        self.layout_principal.addStretch()
        
        # 5. Conecta o evento da ComboBox ao método de exibição
        self.buscar_cidade_combo.currentIndexChanged.connect(self.mostrar_dados_cidade)

    def mostrar_dados_cidade(self):
        """Método que atualiza os rótulos com os dados da cidade selecionada."""
        nome_cidade = self.buscar_cidade_combo.currentText()
        if nome_cidade:
            dados = self.analisador.obter_dados_completos(nome_cidade)
            
            if dados:
                self.municipio_label.setText(f"Município: {nome_cidade}")
                self.mortes_label.setText(f"Mortes: {dados.mortes:,}".replace(",", "."))
                self.casos_label.setText(f"Casos: {dados.casos:,}".replace(",", "."))
                self.letalidade_label.setText(f"Letalidade: {dados.letalidade}%")
            else:
                self.municipio_label.setText("Dados não encontrados.")
                self.mortes_label.setText("")
                self.casos_label.setText("")
                self.letalidade_label.setText("")

