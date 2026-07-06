from model.PagamentoDinheiro import PagamentoDinheiro
from model.PagamentoPix import PagamentoPix
from model.PagamentoCartao import PagamentoCartao
from view.tela_pagamento import TelaPagamento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException
from dao.dao_pagamento import PagamentoDAO  # NOVO (Tarefa 2)


class ControladorPagamento:

    def __init__(self, controlador_sistema):
        self.__dao = PagamentoDAO()  # NOVO (Tarefa 2)
        self.__tela = TelaPagamento()
        self.__controlador_sistema = controlador_sistema
        self.__pagamentos = self.__dao.get_all()  # ALTERADO: antes era [] (Tarefa 2)
        self.__revincular_referencias()  # NOVO (Tarefa 2)

    def __revincular_referencias(self):
        """Reconecta .atendimento de cada pagamento carregado do disco ao
        objeto Atendimento oficial já carregado por controlador_atendimento.py.
        Ver explicação completa no cabeçalho do arquivo. (Tarefa 2)
        """
        ctrl_atendimento = self.__controlador_sistema.controlador_atendimento
        ctrl_paciente = self.__controlador_sistema.controlador_paciente
        atendimentos_oficiais = ctrl_atendimento.get_atendimentos()

        for pagamento in self.__pagamentos:
            atendimento_oficial = self.__buscar_atendimento_equivalente(
                pagamento.atendimento, atendimentos_oficiais
            )
            if atendimento_oficial is not None:
                pagamento.atendimento = atendimento_oficial

            paciente_oficial = ctrl_paciente.buscar_por_cpf(pagamento.paciente.cpf)
            if paciente_oficial is not None:
                pagamento.paciente = paciente_oficial

    def __buscar_atendimento_equivalente(self, referencia, atendimentos: list):
        """Localiza, dentro de uma lista de atendimentos, aquele que
        representa o MESMO atendimento da referência informada, comparando
        clínica (cnpj), paciente (cpf), profissional (cpf), data e hora de
        início — já que Atendimento não possui um ID próprio. (Tarefa 2)
        """
        for atendimento in atendimentos:
            if (atendimento.clinica.cnpj == referencia.clinica.cnpj and
                    atendimento.paciente.cpf == referencia.paciente.cpf and
                    atendimento.profissional.cpf == referencia.profissional.cpf and
                    atendimento.data == referencia.data and
                    atendimento.hora_inicio == referencia.hora_inicio):
                return atendimento
        return None

    def __persistir(self):
        """Grava o estado atual da lista de pagamentos em disco. (Tarefa 2)"""
        self.__dao.save_all(self.__pagamentos)

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao == 1:
                    self.registrar_pagamento()
                elif opcao == 2:
                    self.alterar_pagamento()
                elif opcao == 3:
                    self.listar_pagamentos()
                elif opcao == 4:
                    self.excluir_pagamento()
                elif opcao == 0:
                    break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela.mostra_mensagem(str(e))


    def registrar_pagamento(self):
        ctrl_atendimento = self.__controlador_sistema.controlador_atendimento

        atendimentos = ctrl_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado para pagar.")
            return

        self.__tela.mostra_atendimentos_pendentes(atendimentos)

        indice = self.__tela.seleciona_atendimento()
        if indice < 0 or indice >= len(atendimentos):
            self.__tela.mostra_mensagem("Índice inválido.")
            return

        atendimento = atendimentos[indice]
        paciente = atendimento.paciente

        valor_total = atendimento.valor + atendimento.calcular_total_procedimentos()
        valor_ja_pago = sum(p.valor_pago for p in self.__pagamentos if p.atendimento == atendimento)
        valor_restante = valor_total - valor_ja_pago

        if valor_restante <= 0:
            self.__tela.mostra_mensagem("Este atendimento já está totalmente pago!")
            return

        dados_gerais = self.__tela.pega_dados_pagamento(valor_restante)
        forma = dados_gerais["forma_pagamento"]
        data_pgto = dados_gerais["data_pgto"]
        valor_pago = dados_gerais["valor_pago"]

        if valor_pago > valor_restante:
            self.__tela.mostra_mensagem("Valor pago não pode ser maior que o saldo restante.")
            return

        try:
            if forma == "1":
                dados_extra = self.__tela.pega_dados_dinheiro(valor_pago)
                pagamento = PagamentoDinheiro(
                    data_pgto=data_pgto,
                    atendimento=atendimento,
                    paciente=paciente,
                    valor_pago=valor_pago,
                    quantia_entregue=dados_extra["quantia_entregue"]
                )
            elif forma == "2":
                dados_extra = self.__tela.pega_dados_pix()
                pagamento = PagamentoPix(
                    data_pgto=data_pgto,
                    atendimento=atendimento,
                    paciente=paciente,
                    valor_pago=valor_pago,
                    cpf_pagador=dados_extra["cpf_pagador"]
                )
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
            self.__persistir()  # NOVO (Tarefa 2)
            total_ja_pago = sum(p.valor_pago for p in self.__pagamentos if p.atendimento == atendimento)
            saldo_restante = valor_total - total_ja_pago
            self.__tela.mostra_comprovante(pagamento.emitir_comprovante(saldo_restante))
            self.__tela.mostra_mensagem("Pagamento registrado com sucesso!")

        except (DadoInvalidoException, RegraNegocioException) as e:
            self.__tela.mostra_mensagem(f"Não foi possível registrar o pagamento: {e}")


    def listar_pagamentos(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado.")
            return
        for i, pag in enumerate(self.__pagamentos):
            total_at = pag.atendimento.valor + pag.atendimento.calcular_total_procedimentos()
            pagamentos_do_atendimento = [p for p in self.__pagamentos if p.atendimento == pag.atendimento]
            indice_atual = pagamentos_do_atendimento.index(pag)
            total_pago_ate_aqui = sum(p.valor_pago for p in pagamentos_do_atendimento[:indice_atual + 1])
            saldo = total_at - total_pago_ate_aqui
            self.__tela.mostra_comprovante(f"[{i}] {pag.emitir_comprovante(saldo)}")


    def alterar_pagamento(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado no sistema.")
            return

        self.listar_pagamentos()
        indice = self.__tela.seleciona_pagamento()

        if indice < 0 or indice >= len(self.__pagamentos):
            self.__tela.mostra_mensagem("Índice de pagamento inválido.")
            return

        pagamento_selecionado = self.__pagamentos[indice]
        nova_data = self.__tela.pega_nova_data(pagamento_selecionado)
        if nova_data == '':
            self.__tela.mostra_mensagem("Operação cancelada.")
            return

        try:
            pagamento_selecionado.data = nova_data
            self.__persistir()  # NOVO (Tarefa 2)
            self.__tela.mostra_mensagem("Data do pagamento alterada com sucesso!")
        except (DadoInvalidoException, RegraNegocioException) as e:
            self.__tela.mostra_mensagem(f"Falha ao alterar a data: {e}")


    def excluir_pagamento(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado.")
            return
        self.listar_pagamentos()
        indice = self.__tela.seleciona_pagamento()
        if indice < 0 or indice >= len(self.__pagamentos):
            self.__tela.mostra_mensagem("Índice inválido.")
            return
        self.__pagamentos.pop(indice)
        self.__persistir()  # NOVO (Tarefa 2)
        self.__tela.mostra_mensagem("Pagamento removido.")


    def get_pagamentos(self) -> list:
        return list(self.__pagamentos)

