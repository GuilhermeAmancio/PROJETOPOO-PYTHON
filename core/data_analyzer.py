# Arquivo: core/data_analyzer.py

import os
from .data_model import Municipio, DadosCovid

class AnalisadorDados:
    def __init__(self):
        self.municipios = {}

    def carregar_dados(self, caminho_arquivo: str):
        """
        Lê o arquivo de texto com os dados da COVID-19 e popula
        o dicionário de municípios.
        """
        if not os.path.exists(caminho_arquivo):
            print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
            return

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            blocos = conteudo.split('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
            for bloco in blocos:
                linhas = [linha.strip() for linha in bloco.split('\n') if linha.strip()]
                
                if len(linhas) < 4:
                    continue
                
                nome_municipio = linhas[0]
                
                try:
                    mortes = int(linhas[1].split(':')[1].strip())
                    mortes_por_100k = float(linhas[2].split(':')[1].strip().replace(',', '.'))
                    letalidade = float(linhas[3].split(':')[1].replace('%', '').strip().replace(',', '.'))
                    casos = int(linhas[4].split(':')[1].strip().replace('.', ''))
                    casos_por_100k = float(linhas[5].split(':')[1].strip().replace('.', '').replace(',', '.'))

                    dados_municipio = DadosCovid(mortes, casos, letalidade, mortes_por_100k, casos_por_100k)
                    municipio = Municipio(nome_municipio)
                    municipio.adicionar_dados(dados_municipio)
                    self.municipios[nome_municipio] = municipio
                except (ValueError, IndexError):
                    continue

    def obter_lista_municipios(self) -> list:
        """Retorna uma lista ordenada com os nomes de todos os municípios carregados."""
        return sorted(list(self.municipios.keys()))
    
    def obter_dados_completos(self, nome_municipio: str):
        """Retorna o objeto DadosCovid de um município, se existir."""
        if nome_municipio in self.municipios and self.municipios[nome_municipio].dados_covid:
            return self.municipios[nome_municipio].dados_covid
        return None