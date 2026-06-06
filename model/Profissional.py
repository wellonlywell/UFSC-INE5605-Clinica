# class feita por Well

from model.Pessoa import Pessoa
from model.CorRaca import CorRaca
from typing import Optional
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class Profissional(Pessoa):
    def __init__(self, nome_civil: str, celular: str, cpf: str,
                 especialidade: str, registro: str,
                 nome_social: Optional[str] = None,
                 pcd: bool = False,
                 cor_raca: Optional[CorRaca] = None,
                 identidade_genero: Optional[str] = None):

        # Passando apenas os atributos que a Pessoa possui
        super().__init__(nome_civil, celular, cpf, nome_social, pcd, cor_raca, identidade_genero)

        self.especialidade = especialidade
        self.registro = registro

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Especialidade não pode ser vazia.")
        self.__especialidade = valor.strip()

    @property
    def registro(self) -> str:
        return self.__registro

    @registro.setter
    def registro(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Registro profissional não pode ser vazio.")
        self.__registro = valor.strip()

    def get_info(self) -> str:
        pcd_str = "Sim" if self.pcd else "Não"
        cor = self.cor_raca.value if self.cor_raca else "Não informado"
        genero = self.identidade_genero or "Não informado"
        return (f"Profissional: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Especialidade: {self.__especialidade}\n"
                f"Registro: {self.__registro}\n"
                f"PCD: {pcd_str}\n"
                f"Cor/Raça: {cor}\n"
                f"Identidade de Gênero: {genero}")

    def __str__(self) -> str:
        return f"Profissional: {self.nome} (Especialidade: {self.especialidade})"