
class DadoInvalidoException(Exception):
    """Exceção criada para tratar dados preenchidos incorretamente nos Models."""
    def __init__(self, mensagem):
        super().__init__(mensagem)