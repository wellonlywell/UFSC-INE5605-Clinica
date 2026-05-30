#class feita pelo Marcos


from model.Pagamento import Pagamento
from model.Paciente import Paciente


class PagamentoCartao(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente: Paciente, valor_pago: float,
                 numero_cartao: str, bandeira: str, tipo_cartao: str):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira
        self.tipo_cartao = tipo_cartao
       


    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao


    @numero_cartao.setter
    def numero_cartao(self, valor: str):
        if not isinstance(valor, str) or not valor:
            raise ValueError("Erro: O número do cartão é obrigatório.")
        num_limpo = "".join(c for c in valor if c.isdigit())
        if len(num_limpo) < 13 or len(num_limpo) > 19:
            raise ValueError("Erro: Número de cartão inválido (deve conter entre 13 e 19 dígitos).")
        self.__numero_cartao = num_limpo


    @property
    def bandeira(self) -> str:
        return self.__bandeira


    @bandeira.setter
    def bandeira(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Erro: A bandeira do cartão deve ser informada.")
        self.__bandeira = valor.strip().upper()


    @property
    def tipo_cartao(self) -> str:
        return self.__tipo_cartao


    @tipo_cartao.setter
    def tipo_cartao(self, valor: str):
        opcoes = ["CRÉDITO", "DÉBITO"]
        if not isinstance(valor, str) or valor.upper().strip() not in opcoes:
            raise ValueError("Erro: Tipo de cartão inválido. Escolha 'Crédito' ou 'Débito'.")
        self.__tipo_cartao = valor.upper().strip()


    def __str__(self) -> str:
        return self.emitir_comprovante()


    def emitir_comprovante(self) -> str:
        final_cartao = self.numero_cartao[-4:]
        return (f"--- COMPROVANTE: CARTÃO DE {self.tipo_cartao} ---\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Paciente: {self.paciente.nome}\n"
                f"Bandeira: {self.bandeira} | Cartão: **** **** **** {final_cartao}\n"
                f"Valor Autorizado: R$ {self.valor_pago:.2f}\n"
                f"Débito Restante: R$ {self.valor_restante:.2f}\n"
                f"-------------------------------------------")



PagamentoDinheiro.py
#class feita pelo Marcos


from model.Pagamento import Pagamento
from model.Paciente import Paciente


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
            raise ValueError("Erro: A quantia entregue em dinheiro deve ser um número.")
        if v_float < self.valor_pago:
            raise ValueError(f"Erro: Quantia entregue (R$ {v_float:.2f}) é menor que o valor a ser pago (R$ {self.valor_pago:.2f}).")
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


