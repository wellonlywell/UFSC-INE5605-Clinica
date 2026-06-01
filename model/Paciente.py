from datetime import date
from model.Pessoa import Pessoa
from model.CorRaca import CorRaca
from typing import Optional

class Paciente(Pessoa):
    def __init__(self, nome_civil: str, celular: str, cpf: str,
                 data_nascimento: str,
                 nome_social: Optional[str] = None,
                 responsavel=None,
                 pcd: bool = False,
                 cor_raca: Optional[CorRaca] = None,
                 identidade_genero: Optional[str] = None):
        super().__init__(nome_civil, celular, cpf, nome_social, pcd, cor_raca, identidade_genero)
        self.data_nascimento = data_nascimento
        self.responsavel = responsavel

    # Data de Nascimento
    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        if isinstance(valor, str):
            try:
                dia, mes, ano = map(int, valor.split('/'))
                self.__data_nascimento = date(ano, mes, dia)
            except Exception:
                raise ValueError("Data inválida. Use DD/MM/AAAA.")
        elif isinstance(valor, date):
            self.__data_nascimento = valor
        else:
            raise ValueError("Data inválida.")

    # Idade e Maioridade
    @property
    def idade(self) -> int:
        hoje = date.today()
        anos = hoje.year - self.__data_nascimento.year
        if (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day):
            anos -= 1
        return anos

    @property
    def maior_de_idade(self) -> bool:
        """Regra 1 do enunciado: somente pacientes com mais de 18 anos."""
        return self.idade >= 18

    # Responsável Legal
    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, valor):
        from model.Responsavel import Responsavel
        if valor is not None and not isinstance(valor, Responsavel):
            raise ValueError("Responsável inválido.")
        self.__responsavel = valor

    # Representação
    def get_info(self) -> str:
        resp = self.__responsavel.nome if self.__responsavel else "Nenhum"
        pcd_str = "Sim" if self.pcd else "Não"
        cor = self.cor_raca.value if self.cor_raca else "Não informado"
        genero = self.identidade_genero or "Não informado"
        return (f"Paciente: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Celular: {self.celular}\n"
                f"Idade: {self.idade} anos\n"
                f"Responsável: {resp}\n"
                f"PCD: {pcd_str}\n"
                f"Cor/Raça: {cor}\n"
                f"Identidade de Gênero: {genero}")

    def __str__(self) -> str:
        return f"Paciente: {self.nome} (CPF: {self.cpf})"