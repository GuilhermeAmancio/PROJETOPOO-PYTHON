# Arquivo: ui/data_window.py

from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

# Janela para exibir os dados de COVID-19 de um município.
class DataWindow(QMainWindow):
    def __init__(self, nome_cidade, dados_cidade):
        super().__init__()

        # 1. Configuração da janela
        self.setWindowTitle(f"Dados de {nome_cidade}")
        self.setFixedSize(600, 350)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000;
            }
            QLabel {
                color: #fff;
                font-size: 16px;
                background-color: transparent;
                padding-bottom: 5px;
            }
            #titulo_cidade {
                font-size: 24px;
                font-weight: bold;
                color: #fff;
                padding-bottom: 15px;
            }
        """)

        # 2. Criação dos widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QVBoxLayout(self.central_widget)
        
        # Título da cidade
        self.titulo_cidade_label = QLabel(nome_cidade)
        self.titulo_cidade_label.setObjectName("titulo_cidade")
        self.titulo_cidade_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_principal.addWidget(self.titulo_cidade_label)
        
        # Rótulos para os dados, com formatação corrigida para vírgula
        
        # Formata números inteiros com ponto como separador de milhar.
        self.mortes_label = QLabel(f"Mortes: {dados_cidade.mortes:,}".replace(",", "."))
        self.casos_label = QLabel(f"Casos: {dados_cidade.casos:,}".replace(",", "."))
        
        # Formata números de ponto flutuante com duas casas decimais e vírgula.
        letalidade_formatada = f"{dados_cidade.letalidade:.2f}".replace(".", ",")
        self.letalidade_label = QLabel(f"Letalidade: {letalidade_formatada}%")
        
        mortes_100k_formatado = f"{dados_cidade.mortes_por_100_mil_habitantes:.2f}".replace(".", ",")
        self.mortes_100k_label = QLabel(f"Mortes por 100 mil habitantes: {mortes_100k_formatado}")
        
        # Lógica complexa para formatar um número com separador de milhar e decimal para o padrão brasileiro.
        casos_100k_formatado = f"{dados_cidade.casos_por_100_mil_habitantes:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
        self.casos_100k_label = QLabel(f"Casos por 100 mil habitantes: {casos_100k_formatado}")
        
        # Adiciona os widgets ao layout principal.
        self.layout_principal.addWidget(self.mortes_label)
        self.layout_principal.addWidget(self.casos_label)
        self.layout_principal.addWidget(self.letalidade_label)
        self.layout_principal.addWidget(self.mortes_100k_label)
        self.layout_principal.addWidget(self.casos_100k_label)
        
        self.layout_principal.setAlignment(Qt.AlignmentFlag.AlignCenter)