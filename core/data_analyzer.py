# Arquivo: core/data_analyzer.py

import os
from .data_model import Municipio, DadosCovid

class AnalisadorDados:
    def __init__(self):
        # Dicionário para armazenar os dados de cada município.
        self.municipios = {}

    def carregar_dados(self, caminho_arquivo: str):
        """
        Lê o arquivo de texto com os dados da COVID-19 e popula
        o dicionário de municípios.
        """
        # Verifica se o arquivo existe antes de continuar.
        if not os.path.exists(caminho_arquivo):
            print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
            return

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            # Divide o conteúdo do arquivo em blocos, usando a linha de traços como separador.
            blocos = conteudo.split('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
            for bloco in blocos:
                # Processa cada linha do bloco, removendo espaços e linhas vazias.
                linhas = [linha.strip() for linha in bloco.split('\n') if linha.strip()]
                
                # Pula blocos que não contêm dados suficientes.
                if len(linhas) < 4:
                    continue
                
                nome_municipio = linhas[0]
                
                # Tenta extrair os dados e criar os objetos.
                try:
                    # Extração e conversão dos dados para os tipos corretos (int, float).
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
                    # Em caso de erro na extração dos dados, o bloco é ignorado.
                    continue

    def obter_lista_municipios(self) -> list:
        """Retorna uma lista ordenada com os nomes de todos os municípios carregados."""
        return sorted(list(self.municipios.keys()))
    
    def obter_dados_completos(self, nome_municipio: str):
        """Retorna o objeto DadosCovid de um município, se existir."""
        # Verifica se o município existe e se tem dados antes de retorná-los.
        if nome_municipio in self.municipios and self.municipios[nome_municipio].dados_covid:
            return self.municipios[nome_municipio].dados_covid
        return None