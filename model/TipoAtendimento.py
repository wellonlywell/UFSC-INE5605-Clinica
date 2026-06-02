# class feita por Well

# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException


class TipoAtendimento:
    def __init__(self, descricao: str):
        self.descricao = descricao

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Descrição do tipo de atendimento não pode ser vazia.")
        self.__descricao = valor.strip()

    def __str__(self) -> str:
        return self.__descricao
