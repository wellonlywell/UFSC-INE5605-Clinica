class PagamentoCartao(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente, valor_pago: float, numero_cartao: str, bandeira: str, tipo_cartao: str):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira
        self.tipo_cartao = tipo_cartao