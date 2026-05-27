class PagamentoPix(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.cpf_pagador = cpf_pagador