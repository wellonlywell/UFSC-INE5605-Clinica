class Clinica:
    def __init__(self, cnpj: str, nome: str, localizacao: str, cidade: str, descricao: str):
        self.cnpj = cnpj
        self.nome = nome
        self.localizacao = localizacao
        self.cidade = cidade
        self.descricao = descricao