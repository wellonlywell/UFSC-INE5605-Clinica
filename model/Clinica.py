from datetime import time
from model.Profissional import Profissional
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class Clinica:
    def __init__(self, cnpj: str, nome: str, cidade: str,
                 descricao: str, horario_abertura: str, horario_fechamento: str):
        self.cnpj = cnpj
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento
        self.__profissionais = []  # AGREGAÇÃO: profissionais existem fora da clínica


    @property
    def cnpj(self) -> str:
        return self.__cnpj


    @cnpj.setter
    def cnpj(self, valor: str):
        if not isinstance(valor, str):
            raise DadoInvalidoException("Erro: CNPJ deve ser uma string.")
        cnpj_limpo = "".join(c for c in valor if c.isdigit())
        if len(cnpj_limpo) != 14:
            raise DadoInvalidoException("Erro: CNPJ deve ter 14 dígitos.")
        self.__cnpj = valor


    @property
    def nome(self) -> str:
        return self.__nome


    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Erro: Nome da clínica não pode ser vazio.")
        self.__nome = valor.strip()


   
    @property
    def cidade(self) -> str:
        return self.__cidade


    @cidade.setter
    def cidade(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Erro: Cidade não pode ser vazia.")
        self.__cidade = valor.strip()


    @property
    def descricao(self) -> str:
        return self.__descricao


    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException("Erro: Descrição não pode ser vazia.")
        self.__descricao = valor.strip()


    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura


    @horario_abertura.setter
    def horario_abertura(self, valor):
        if isinstance(valor, str):
            try:
                h, m = map(int, valor.split(':'))
                self.__horario_abertura = time(h, m)
            except Exception:
                raise DadoInvalidoException("Erro: Horário inválido. Use HH:MM.")
        elif isinstance(valor, time):
            self.__horario_abertura = valor
        else:
            raise DadoInvalidoException("Erro: Horário inválido.")


    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento


    @horario_fechamento.setter
    def horario_fechamento(self, valor):
        if isinstance(valor, str):
            try:
                h, m = map(int, valor.split(':'))
                t = time(h, m)
            except Exception:
                raise DadoInvalidoException("Erro: Horário inválido. Use HH:MM.")
        elif isinstance(valor, time):
            t = valor
        else:
            raise DadoInvalidoException("Erro: Horário inválido.")
        # Validação cruzada: fechamento deve ser após abertura
        if hasattr(self, '_Clinica__horario_abertura') and t <= self.__horario_abertura:
            raise DadoInvalidoException("Erro: Horário de fechamento deve ser posterior ao de abertura.")
        self.__horario_fechamento = t


    # Profissionais (AGREGAÇÃO)
    @property
    def profissionais(self) -> list:
        return list(self.__profissionais)  # retorna cópia para proteger a lista interna


    def adicionar_profissional(self, profissional: Profissional):
        """AGREGAÇÃO: adiciona profissional à clínica. Ele pode existir sem ela."""
        if not isinstance(profissional, Profissional):
            raise DadoInvalidoException("Erro: Profissional inválido.")
        if profissional in self.__profissionais:
            raise DadoInvalidoException("Erro: Profissional já cadastrado nesta clínica.")
        self.__profissionais.append(profissional)


    def remover_profissional(self, profissional: Profissional):
        """AGREGAÇÃO: remove da clínica, mas profissional continua existindo no sistema."""
        if profissional not in self.__profissionais:
            raise DadoInvalidoException("Erro: Profissional não encontrado nesta clínica.")
        self.__profissionais.remove(profissional)


    def esta_aberta(self, horario: time) -> bool:
        """Verifica se a clínica está aberta no horário informado (usada na Regra 2)."""
        return self.__horario_abertura <= horario <= self.__horario_fechamento


    def __str__(self) -> str:
        n_profs = len(self.__profissionais)
        return (f"Clínica: {self.__nome}\n"
                f"CNPJ: {self.__cnpj}\n"
                f"Cidade: {self.__cidade}\n"
                f"Descrição: {self.__descricao}\n"
                f"Funcionamento: {self.__horario_abertura.strftime('%H:%M')} às {self.__horario_fechamento.strftime('%H:%M')}\n"
                f"Profissionais cadastrados: {n_profs}")
