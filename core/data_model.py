# Arquivo: core/data_model.py

class DadosCovid:
    def __init__(self, mortes: int, casos: int, letalidade: float):
        self.mortes = mortes
        self.casos = casos
        self.letalidade = letalidade

    def __repr__(self):
        return f"<DadosCovid mortes={self.mortes} casos={self.casos} letalidade={self.letalidade}%>"

class Municipio:
    def __init__(self, nome: str):
        self.nome = nome
        self.dados_covid = None # Será um objeto da classe DadosCovid

    def adicionar_dados(self, dados: DadosCovid):
        self.dados_covid = dados

    def __repr__(self):
        return f"<Municipio nome='{self.nome}'>"