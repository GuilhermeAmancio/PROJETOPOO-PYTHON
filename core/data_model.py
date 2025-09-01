# Arquivo: core/data_model.py

# A classe DadosCovid representa e armazena os dados estatísticos da COVID-19.
class DadosCovid:
    def __init__(self, mortes: int, casos: int, letalidade: float, mortes_por_100_mil_habitantes: float, casos_por_100_mil_habitantes: float):
        self.mortes = mortes
        self.casos = casos
        self.letalidade = letalidade
        self.mortes_por_100_mil_habitantes = mortes_por_100_mil_habitantes
        self.casos_por_100_mil_habitantes = casos_por_100_mil_habitantes

    # Permite uma representação de string amigável para a classe, útil para depuração.
    def __repr__(self):
        return f"<DadosCovid mortes={self.mortes} casos={self.casos} letalidade={self.letalidade}%>"

# A classe Municipio representa uma entidade geográfica e seus dados de COVID-19.
class Municipio:
    def __init__(self, nome: str):
        self.nome = nome
        # O atributo é inicializado como None e depois recebe um objeto DadosCovid.
        self.dados_covid = None

    # Método para associar um objeto DadosCovid a um objeto Municipio.
    def adicionar_dados(self, dados: DadosCovid):
        self.dados_covid = dados

    # Permite uma representação de string amigável para a classe.
    def __repr__(self):
        return f"<Municipio nome='{self.nome}'>"