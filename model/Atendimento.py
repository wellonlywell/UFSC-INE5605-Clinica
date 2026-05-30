from datetime import date, time
from model.Clinica import Clinica
from model.Paciente import Paciente
from model.Profissional import Profissional
from model.Procedimento import Procedimento
from model.TipoAtendimento import TipoAtendimento


class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional,
                 data: str, hora_inicio: str, hora_fim: str,
                 tipo: TipoAtendimento, valor: float):
        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.tipo = tipo
        self.valor = valor
        self.__procedimentos = []


    @property
    def clinica(self) -> Clinica:
        return self.__clinica


    @clinica.setter
    def clinica(self, valor):
        if not isinstance(valor, Clinica):
            raise ValueError("Erro: Clínica inválida.")
        self.__clinica = valor


    @property
    def paciente(self) -> Paciente:
        return self.__paciente


    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise ValueError("Erro: Paciente inválido.")
        # Regra 1: menor de idade só com responsável vinculado
        if not valor.maior_de_idade and valor.responsavel is None:
            raise ValueError("Erro: Paciente menor de idade deve ter um responsável cadastrado.")
        self.__paciente = valor


    @property
    def profissional(self) -> Profissional:
        return self.__profissional


    @profissional.setter
    def profissional(self, valor):
        if not isinstance(valor, Profissional):
            raise ValueError("Erro: Profissional inválido.")
        self.__profissional = valor


    @property
    def data(self) -> date:
        return self.__data


    @data.setter
    def data(self, valor):
        if isinstance(valor, str):
            try:
                dia, mes, ano = map(int, valor.split('/'))
                self.__data = date(ano, mes, dia)
            except Exception:
                raise ValueError("Erro: Use o formato DD/MM/AAAA.")
        elif isinstance(valor, date):
            self.__data = valor
        else:
            raise ValueError("Erro: Data inválida.")


    @property
    def hora_inicio(self) -> time:
        return self.__hora_inicio


    @hora_inicio.setter
    def hora_inicio(self, valor):
        if isinstance(valor, str):
            try:
                h, m = map(int, valor.split(':'))
                t = time(h, m)
            except Exception:
                raise ValueError("Erro: Use o formato HH:MM.")
        elif isinstance(valor, time):
            t = valor
        else:
            raise ValueError("Erro: Hora inválida.")
        # Regra 2: atendimento deve estar dentro do funcionamento da clínica
        if hasattr(self, '_Atendimento__clinica') and not self.__clinica.esta_aberta(t):
            raise ValueError("Erro: Horário fora do funcionamento da clínica.")
        self.__hora_inicio = t


    @property
    def hora_fim(self) -> time:
        return self.__hora_fim


    @hora_fim.setter
    def hora_fim(self, valor):
        if isinstance(valor, str):
            try:
                h, m = map(int, valor.split(':'))
                t = time(h, m)
            except Exception:
                raise ValueError("Erro: Use o formato HH:MM.")
        elif isinstance(valor, time):
            t = valor
        else:
            raise ValueError("Erro: Hora inválida.")
        # Regra 2: atendimento deve estar dentro do funcionamento da clínica
        if hasattr(self, '_Atendimento__clinica') and not self.__clinica.esta_aberta(t):
            raise ValueError("Erro: Horário fora do funcionamento da clínica.")
        if hasattr(self, '_Atendimento__hora_inicio') and t <= self.__hora_inicio:
            raise ValueError("Erro: Hora de fim deve ser posterior à hora de início.")
        self.__hora_fim = t


    @property
    def tipo(self) -> TipoAtendimento:
        return self.__tipo


    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, TipoAtendimento):
            raise ValueError("Erro: Tipo de atendimento inválido.")
        self.__tipo = valor


    @property
    def valor(self) -> float:
        return self.__valor


    @valor.setter
    def valor(self, valor):
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise ValueError("Erro: Valor deve ser numérico.")
        if v <= 0:
            raise ValueError("Erro: Valor deve ser maior que zero.")
        self.__valor = v


    @property
    def procedimentos(self) -> list:
        return list(self.__procedimentos)


    def adicionar_procedimento(self, descricao: str, custo: float, profissional: Profissional):
        """COMPOSIÇÃO: Procedimento é criado aqui dentro — não existe fora do Atendimento."""
        novo_procedimento = Procedimento(descricao, custo, profissional)
        self.__procedimentos.append(novo_procedimento)




    def calcular_total_procedimentos(self) -> float:
        """Retorna a soma dos custos de todos os procedimentos do atendimento."""
        return sum(p.custo for p in self.__procedimentos)


    def remover_procedimento(self, procedimento: Procedimento):
        if procedimento not in self.__procedimentos:
            raise ValueError("Erro: Procedimento não encontrado.")
        self.__procedimentos.remove(procedimento)


    def __str__(self) -> str:
        procs = "\n  ".join(str(p) for p in self.__procedimentos) if self.__procedimentos else "Nenhum"
        return (f"Atendimento - Clínica: {self.__clinica.nome}\n"
                f"Paciente: {self.__paciente.nome}\n"
                f"Profissional: {self.__profissional.nome}\n"
                f"Data e Horário: {self.__data.strftime('%d/%m/%Y')} às {self.__hora_inicio.strftime('%H:%M')}\n"
                f"Valor Total: R$ {self.__valor:.2f}\n"
                f"Procedimentos: {procs}")


