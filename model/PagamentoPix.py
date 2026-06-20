from model.Pagamento import Pagamento
from model.Paciente import Paciente
from exceptions.dado_invalido_exception import DadoInvalidoException

class PagamentoPix(Pagamento):
    def __init__(self, data_pgto, atendimento, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pgto, atendimento, paciente, valor_pago)
        self.cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, valor: str):
        if not isinstance(valor, str):
            raise DadoInvalidoException("Erro: CPF do pagador deve ser uma string.")
        digitos = "".join(c for c in valor if c.isdigit())
        if len(digitos) != 11:
            raise DadoInvalidoException("Erro: CPF do pagador deve ter 11 dígitos.")
        self.__cpf_pagador = valor


    def __str__(self) -> str:
        return self.emitir_comprovante()


    def emitir_comprovante(self, valor_restante: float = 0.0) -> str:
        return (f"--- COMPROVANTE: PIX ---\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Paciente: {self.paciente.nome}\n"
                f"CPF Pagador: {self.__cpf_pagador}\n"
                f"Valor Pago: R$ {self.valor_pago:.2f}\n"
                f"Débito Restante: R$ {valor_restante:.2f}\n"
                f"------------------------")
