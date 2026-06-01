


class TipoAtendimento:
    def __init__(self, descricao: str):
        self.descricao = descricao

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Descrição do tipo de atendimento não pode ser vazia.")
        self.__descricao = valor.strip()

    def __str__(self) -> str:
        return self.__descricao
