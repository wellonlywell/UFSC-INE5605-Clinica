from datetime import date, time
from model.Clinica import Clinica
from model.Paciente import Paciente
from model.Profissional import Profissional
from model.ItemProcedimento import ItemProcedimento
from model.TipoAtendimento import TipoAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException# Exceptions customizadas, validações de dado movidas para a pasta exceptions


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
        self.__item_procedimentos = []


    @property
    def clinica(self) -> Clinica:
        return self.__clinica


    @clinica.setter
    def clinica(self, valor):
        if not isinstance(valor, Clinica):
            raise DadoInvalidoException("Erro: Clínica inválida.")
        self.__clinica = valor


    @property
    def paciente(self) -> Paciente:
        return self.__paciente


    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise DadoInvalidoException("Erro: Paciente inválido.")
        self.__paciente = valor


    @property
    def profissional(self) -> Profissional:
        return self.__profissional


    @profissional.setter
    def profissional(self, valor):
        if not isinstance(valor, Profissional):
            raise DadoInvalidoException("Erro: Profissional inválido.")
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
                raise DadoInvalidoException("Erro: Use o formato DD/MM/AAAA.")
        elif isinstance(valor, date):
            self.__data = valor
        else:
            raise DadoInvalidoException("Erro: Data inválida.")


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
                raise DadoInvalidoException("Erro: Use o formato HH:MM.")
        elif isinstance(valor, time):
            t = valor
        else:
            raise DadoInvalidoException("Erro: Hora inválida.")
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
                raise DadoInvalidoException("Erro: Use o formato HH:MM.")
        elif isinstance(valor, time):
            t = valor
        else:
            raise DadoInvalidoException("Erro: Hora inválida.")
        # Garante que o fim não seja menor ou igual ao início
        if hasattr(self, '_Atendimento__hora_inicio') and t <= self.__hora_inicio:
            raise DadoInvalidoException("Erro: Hora de fim deve ser posterior à hora de início.")
        self.__hora_fim = t


    @property
    def tipo(self) -> TipoAtendimento:
        return self.__tipo


    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, TipoAtendimento):
            raise DadoInvalidoException("Erro: Tipo de atendimento inválido.")
        self.__tipo = valor


    @property
    def valor(self) -> float:
        return self.__valor


    @valor.setter
    def valor(self, valor):
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise DadoInvalidoException("Erro: Valor deve ser numérico.")
        if v <= 0:
            raise DadoInvalidoException("Erro: Valor deve ser maior que zero.")
        self.__valor = v


    @property
    def procedimentos(self) -> list:
        return list(self.__item_procedimentos)


    def adicionar_procedimento(self, descricao: str, custo: float, profissional: Profissional):
        """COMPOSIÇÃO: item é criado aqui dentro, não existe fora do Atendimento, seria tipo um procedimento específico daquele atendimento, como item numa nota fiscal. Vc tem  catalgo geral mas tem a item espcifico no seu atendimento."""
        novo_item = ItemProcedimento(descricao, custo, profissional)
        self.__item_procedimentos.append(novo_item)


    def calcular_total_procedimentos(self) -> float:
        """Retorna a soma dos custos de todos os procedimentos do atendimento."""
        return sum(p.custo for p in self.__item_procedimentos)


    def remover_procedimento(self, item: ItemProcedimento):
        if item not in self.__item_procedimentos:
            raise DadoInvalidoException("Erro: Procedimento não encontrado.")
        self.__item_procedimentos.remove(item)


    def __str__(self) -> str:
        procs = "\n  ".join(str(p) for p in self.__item_procedimentos) if self.__item_procedimentos else "Nenhum"
        return (f"Atendimento - Clínica: {self.__clinica.nome}\n"
                f"Paciente: {self.__paciente.nome}\n"
                f"Profissional: {self.__profissional.nome}\n"
                f"Data e Horário: {self.__data.strftime('%d/%m/%Y')} às {self.__hora_inicio.strftime('%H:%M')}\n"
                f"Valor Total: R$ {self.__valor:.2f}\n"
                f"Procedimentos realizados: {procs}")


