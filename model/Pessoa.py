# class feita por Well

from abc import ABC, abstractmethod
from typing import Optional
from model.cor_raca import CorRaca
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class Pessoa(ABC):
    def __init__(self, nome_civil: str, celular: str, cpf: str,
                 nome_social: Optional[str] = None,
                 pcd: bool = False,
                 cor_raca: Optional[CorRaca] = None,
                 identidade_genero: Optional[str] = None):
        self.nome_civil = nome_civil
        self.celular = celular
        self.cpf = cpf
        self.nome_social = nome_social
        self.pcd = pcd
        self.cor_raca = cor_raca
        self.identidade_genero = identidade_genero

    @property
    def nome(self) -> str:
        """Retorna nome social se existir, senão nome civil (nome social garantido pela Lei 8.727/2016)."""
        if self.__nome_social:
            return self.__nome_social
        return self.__nome_civil

    @property
    def nome_civil(self) -> str:
        return self.__nome_civil

    @nome_civil.setter
    def nome_civil(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Nome civil não pode ser vazio.")
        self.__nome_civil = valor.strip()

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, valor: str):
        if not isinstance(valor, str):
            raise DadoInvalidoException("Celular deve ser uma string.")
        digitos = "".join(c for c in valor if c.isdigit())
        if len(digitos) < 10 or len(digitos) > 11:
            raise DadoInvalidoException("Celular inválido.")
        self.__celular = valor

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, valor: str):
        if not isinstance(valor, str):
            raise DadoInvalidoException("CPF deve ser uma string.")
        digitos = "".join(c for c in valor if c.isdigit())
        if len(digitos) != 11:
            raise DadoInvalidoException("CPF deve ter 11 dígitos.")
        self.__cpf = valor

    @property
    def nome_social(self) -> Optional[str]:
        return self.__nome_social

    @nome_social.setter
    def nome_social(self, valor):
        if valor is not None and not isinstance(valor, str):
            raise DadoInvalidoException("Nome social deve ser uma string.")
        self.__nome_social = valor.strip() if valor else None

    @property
    def pcd(self) -> bool:
        return self.__pcd

    @pcd.setter
    def pcd(self, valor: bool):
        if not isinstance(valor, bool):
            raise DadoInvalidoException("PCD deve ser verdadeiro ou falso.")
        self.__pcd = valor

    @property
    def cor_raca(self) -> Optional[CorRaca]:
        return self.__cor_raca

    @cor_raca.setter
    def cor_raca(self, valor):
        if valor is not None and not isinstance(valor, CorRaca):
            raise DadoInvalidoException("Cor/Raça inválida.")
        self.__cor_raca = valor

    @property
    def identidade_genero(self) -> Optional[str]:
        return self.__identidade_genero

    @identidade_genero.setter
    def identidade_genero(self, valor):
        if valor is not None and not isinstance(valor, str):
            raise DadoInvalidoException("Identidade de gênero deve ser uma string.")
        self.__identidade_genero = valor.strip() if valor else None

    @abstractmethod
    def get_info(self) -> str:
        """Método abstrato que obriga os filhos (Paciente/Profissional/Responsável) a implementarem."""
        pass