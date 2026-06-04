#class feita pelo Marcos

from model.pagamento import Pagamento
from model.paciente import Paciente
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente: Paciente, valor_pago: float, quantia_entregue: float):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.quantia_entregue = quantia_entregue


    @property
    def quantia_entregue(self) -> float:
        return self.__quantia_entregue


    @quantia_entregue.setter
    def quantia_entregue(self, valor):
        try:
            v_float = float(valor)
        except (ValueError, TypeError):
            raise DadoInvalidoException("Erro: A quantia entregue em dinheiro deve ser um número.")
        if v_float < self.valor_pago:
            raise DadoInvalidoException(f"Erro: Quantia entregue (R$ {v_float:.2f}) é menor que o valor a ser pago (R$ {self.valor_pago:.2f}).")
        self.__quantia_entregue = v_float


    @property
    def troco(self) -> float:
        return self.quantia_entregue - self.valor_pago


    def __str__(self) -> str:
        return self.emitir_comprovante()


    def emitir_comprovante(self) -> str:
        return (f"--- COMPROVANTE: DINHEIRO ---\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Paciente: {self.paciente.nome}\n"
                f"Valor Pago: R$ {self.valor_pago:.2f}\n"
                f"Quantia Entregue: R$ {self.quantia_entregue:.2f}\n"
                f"Troco: R$ {self.troco:.2f}\n"
                f"Débito Restante: R$ {self.valor_restante:.2f}\n"
                f"-----------------------------")


