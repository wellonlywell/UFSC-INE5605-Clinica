# class feita por Well

from model.Profissional import Profissional
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Descrição não pode ser vazia.")
        self.__descricao = valor.strip()

    @property
    def custo(self) -> float:
        return self.__custo

    @custo.setter
    def custo(self, valor):
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise DadoInvalidoException("Custo deve ser um número.")
        if v < 0:
            raise DadoInvalidoException("Custo não pode ser negativo.")
        self.__custo = v

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, valor):
        if not isinstance(valor, Profissional):
            raise DadoInvalidoException("Profissional inválido.")
        self.__profissional = valor

    def __str__(self) -> str:
        return (f"Procedimento: {self.__descricao}\n"
                f"Custo: R$ {self.__custo:.2f}\n"
                f"Responsável: {self.__profissional.nome}")
