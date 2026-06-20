# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException


class TipoAtendimento:
    def __init__(self, id: int, descricao: str):
        self.id = id
        self.descricao = descricao

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise DadoInvalidoException("ID deve ser um inteiro positivo.")
        self.__id = valor

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Descrição do tipo de atendimento não pode ser vazia.")
        self.__descricao = valor.strip()

    def __str__(self) -> str:
        return f"{self.__id} - {self.__descricao}"
