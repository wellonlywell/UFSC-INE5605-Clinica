class Pagamento(ABC):
    def __init__(self, data_pgto, atendimento: Atendimento, paciente: str, valor_pago: float):
        self.atendimento = atendimento
        self.data = data_pgto
        self.paciente = paciente
        self.valor_pago = valor_pago
