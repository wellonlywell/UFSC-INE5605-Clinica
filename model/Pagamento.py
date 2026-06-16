from abc import ABC, abstractmethod
from datetime import date
from model.Paciente import Paciente
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException


class Pagamento(ABC):  # CLASSE ABSTRATA — critério avaliação: herança e classes abstratas
    def __init__(self, data_pgto, atendimento, paciente: Paciente, valor_pago: float):
        self.atendimento = atendimento  # ASSOCIAÇÃO com Atendimento (setado antes da data)
        self.data = data_pgto           # valida Regra 3 após atendimento estar setado
        self.paciente = paciente        # ASSOCIAÇÃO com Paciente
        self.valor_pago = valor_pago


    @property
    def data(self) -> date:
        return self.__data


    @data.setter
    def data(self, valor):
        if isinstance(valor, str):
            try:
                dia, mes, ano = map(int, valor.split('/'))
                d = date(ano, mes, dia)
            except Exception:
                raise DadoInvalidoException("Erro: Data inválida. Use DD/MM/AAAA.")
        elif isinstance(valor, date):
            d = valor
        else:
            raise DadoInvalidoException("Erro: Data inválida.")
        # Só podemos verificar se o atendimento já foi salvo no objeto (e foi, lá no __init__)
        if hasattr(self, 'atendimento') and self.atendimento is not None:
            data_atendimento = self.atendimento.data
            
            # Se a data de pagamento for maior que a data do atendimento, é uma violação da regra de negócio!
            if d > data_atendimento:
                raise RegraNegocioException(
                    f"Violação de Regra: O pagamento (data: {d.strftime('%d/%m/%Y')}) "
                    f"deve ser realizado até a data do atendimento ({data_atendimento.strftime('%d/%m/%Y')})."
                )        
        # Se passou em todas as verificações, salva a data.
        self.__data = d


    @property
    def atendimento(self):
        return self.__atendimento


    @atendimento.setter
    def atendimento(self, valor):
        if not valor or not hasattr(valor, 'valor'):
            raise DadoInvalidoException("Erro: Atendimento inválido.")
        self.__atendimento = valor


    @property
    def paciente(self) -> Paciente:
        return self.__paciente


    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise DadoInvalidoException("Erro: Paciente inválido.")
        self.__paciente = valor


    @property
    def valor_pago(self) -> float:
        return self.__valor_pago


    @valor_pago.setter
    def valor_pago(self, valor):
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise DadoInvalidoException("Erro: Valor pago deve ser um número.")
        if v <= 0:
            raise DadoInvalidoException("Erro: Valor pago deve ser maior que zero.")
        self.__valor_pago = v
    

    @abstractmethod  # MÉTODO ABSTRATO: cada modalidade implementa seu comprovante
    def emitir_comprovante(self) -> str:
        pass
