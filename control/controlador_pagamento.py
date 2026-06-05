from model.PagamentoDinheiro import PagamentoDinheiro
from model.PagamentoPix import PagamentoPix
from model.PagamentoCartao import PagamentoCartao
from view.tela_pagamento import TelaPagamento
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorPagamento:
    """
    Gerencia todos os pagamentos do sistema.
    
    """

    def __init__(self, controlador_sistema):
        self.__pagamentos = []
        self.__tela = TelaPagamento()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 1:
                self.registrar_pagamento()
            elif opcao == 2:
                self.listar_pagamentos()
            elif opcao == 3:
                self.excluir_pagamento()
            elif opcao == 0:
                break

    def registrar_pagamento(self):
        """
        Pede os dados gerais, escolhe a modalidade e cria o objeto certo.
        
        """
        ctrl_atendimento = self.__controlador_sistema.controlador_atendimento
        ctrl_paciente = self.__controlador_sistema.controlador_paciente

        atendimentos = ctrl_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado para pagar.")
            return

        # Mostra atendimentos disponíveis
        for i, at in enumerate(atendimentos):
            print(f"[{i}] {at.paciente.nome} - R$ {at.valor:.2f} - {at.data.strftime('%d/%m/%Y')}")

        indice = self.__tela.seleciona_atendimento()
        if indice < 0 or indice >= len(atendimentos):
            self.__tela.mostra_mensagem("Índice inválido.")
            return
        atendimento = atendimentos[indice]
        paciente = atendimento.paciente

        dados_gerais = self.__tela.pega_dados_pagamento(atendimento.valor)
        forma = dados_gerais["forma_pagamento"]
        data_pgto = dados_gerais["data_pgto"]
        valor_pago = dados_gerais["valor_pago"]

        try:
            # --- DINHEIRO ---
            if forma == "1":
                dados_extra = self.__tela.pega_dados_dinheiro(valor_pago)
                pagamento = PagamentoDinheiro(
                    data_pgto=data_pgto,
                    atendimento=atendimento,
                    paciente=paciente,
                    valor_pago=valor_pago,
                    quantia_entregue=dados_extra["quantia_entregue"]
                )

            # --- PIX ---
            elif forma == "2":
                dados_extra = self.__tela.pega_dados_pix()
                pagamento = PagamentoPix(
                    data_pgto=data_pgto,
                    atendimento=atendimento,
                    paciente=paciente,
                    valor_pago=valor_pago,
                    cpf_pagador=dados_extra["cpf_pagador"]
                )

            # --- CARTÃO ---
            elif forma == "3":
                dados_extra = self.__tela.pega_dados_cartao()
                pagamento = PagamentoCartao(
                    data_pgto=data_pgto,
                    atendimento=atendimento,
                    paciente=paciente,
                    valor_pago=valor_pago,
                    numero_cartao=dados_extra["numero_cartao"],
                    bandeira=dados_extra["bandeira"],
                    tipo_cartao=dados_extra["tipo_cartao"]
                )
            else:
                self.__tela.mostra_mensagem("Opção de pagamento inválida.")
                return

            self.__pagamentos.append(pagamento)
            # Exibe o comprovante logo após o registro
            print("\n" + pagamento.emitir_comprovante())
            self.__tela.mostra_mensagem("Pagamento registrado com sucesso!")

        except DadoInvalidoException as e:
            self.__tela.mostra_mensagem(f"Erro nos dados: {e}")

    def listar_pagamentos(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado.")
            return
        for i, pag in enumerate(self.__pagamentos):
            print(f"\n[{i}] {pag.emitir_comprovante()}")

    def excluir_pagamento(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado.")
            return
        self.listar_pagamentos()
        indice = self.__tela.seleciona_pagamento()
        if indice < 0 or indice >= len(self.__pagamentos):
            self.__tela.mostra_mensagem("Índice inválido.")
            return
        self.__pagamentos.remove(self.__pagamentos[indice])
        self.__tela.mostra_mensagem("Pagamento removido.")

    def get_pagamentos(self) -> list:
        return list(self.__pagamentos)
