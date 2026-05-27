class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente, valor_pago: float, quantia_entregue: float):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.quantia_entregue = quantia_entregue
