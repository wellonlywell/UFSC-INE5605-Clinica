from model.Atendimento import Atendimento
from view.tela_atendimento import TelaAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException
from dao.dao_atendimento import AtendimentoDAO  # NOVO (Tarefa 2)
from datetime import time as Time


class ControladorAtendimento:

    def __init__(self, controlador_sistema):
        self.__dao = AtendimentoDAO()  # NOVO (Tarefa 2)
        self.__tela = TelaAtendimento()
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = self.__dao.get_all()  # ALTERADO: antes era [] (Tarefa 2)
        self.__revincular_referencias()  # NOVO (Tarefa 2)

    def __revincular_referencias(self):
        """Reconecta .clinica e .tipo de cada atendimento carregado do disco
        aos objetos oficiais já carregados pelos respectivos controladores.
        Ver explicação completa no cabeçalho do arquivo. (Tarefa 2)
        """
        ctrl_clinica = self.__controlador_sistema.controlador_clinica
        ctrl_tipo = self.__controlador_sistema.controlador_tipo_atendimento
        ctrl_paciente = self.__controlador_sistema.controlador_paciente
        ctrl_profissional = self.__controlador_sistema.controlador_profissional

        for atendimento in self.__atendimentos:
            clinica_oficial = ctrl_clinica.buscar_por_cnpj(atendimento.clinica.cnpj)
            if clinica_oficial is not None:
                atendimento.clinica = clinica_oficial

            tipo_oficial = ctrl_tipo.buscar_por_id(atendimento.tipo.id)
            if tipo_oficial is not None:
                atendimento.tipo = tipo_oficial

            paciente_oficial = ctrl_paciente.buscar_por_cpf(atendimento.paciente.cpf)
            if paciente_oficial is not None:
                atendimento.paciente = paciente_oficial

            profissional_oficial = ctrl_profissional.buscar_por_cpf(atendimento.profissional.cpf)
            if profissional_oficial is not None:
                atendimento.profissional = profissional_oficial

    def __persistir(self):
        """Grava o estado atual da lista de atendimentos em disco. (Tarefa 2)"""
        self.__dao.save_all(self.__atendimentos)

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao == 1:
                    self.incluir_atendimento()
                elif opcao == 2:
                    self.alterar_atendimento()
                elif opcao == 3:
                    self.listar_atendimentos()
                elif opcao == 4:
                    self.excluir_atendimento()
                elif opcao == 5:
                    self.registrar_procedimento()
                elif opcao == 0:
                    break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela.mostra_mensagem(str(e))

    def __verifica_regra2(self, clinica, hora_inicio_str: str, hora_fim_str: str):

        try:
            h_i, m_i = map(int, hora_inicio_str.split(":"))
            h_f, m_f = map(int, hora_fim_str.split(":"))
            inicio = Time(h_i, m_i)
            fim    = Time(h_f, m_f)
        except ValueError:
            raise DadoInvalidoException(
                "Hora inválida. Use o formato HH:MM (ex: 14:30)."
            )

            if not clinica.esta_aberta(inicio) or not clinica.esta_aberta(fim):
                abertura   = clinica.horario_abertura.strftime("%H:%M")
                fechamento = clinica.horario_fechamento.strftime("%H:%M")
                raise RegraNegocioException(
                    f"REGRA 2 VIOLADA: O atendimento ({hora_inicio_str} - {hora_fim_str}) "
                    f"deve ocorrer inteiramente dentro do horário da clínica ({abertura} - {fechamento})."
                )

    def incluir_atendimento(self):
        dados = self.__tela.pega_dados_atendimento()

        ctrl_clinica      = self.__controlador_sistema.controlador_clinica
        ctrl_paciente     = self.__controlador_sistema.controlador_paciente
        ctrl_profissional = self.__controlador_sistema.controlador_profissional
        ctrl_tipo         = self.__controlador_sistema.controlador_tipo_atendimento

        clinica = ctrl_clinica.buscar_por_cnpj(dados["cnpj_clinica"])
        if clinica is None:
            self.__tela.mostra_mensagem("Clínica não encontrada. Cadastre-a primeiro.")
            return

        paciente = ctrl_paciente.buscar_por_cpf(dados["cpf_paciente"])
        if paciente is None:
            self.__tela.mostra_mensagem("Paciente não encontrado. Cadastre-o primeiro.")
            return

        profissional = ctrl_profissional.buscar_por_cpf(dados["cpf_profissional"])
        if profissional is None:
            self.__tela.mostra_mensagem("Profissional não encontrado. Cadastre-o primeiro.")
            return

        tipo = ctrl_tipo.buscar_por_descricao(dados["descricao_tipo"])
        if tipo is None:
            self.__tela.mostra_mensagem("Tipo de atendimento não encontrado. Cadastre-o primeiro.")
            return

        if not paciente.maior_de_idade and paciente.responsavel is None:
            self.__tela.mostra_mensagem(
                f"REGRA 1 VIOLADA: O paciente tem {paciente.idade} anos (menor de idade) "
                "e não possui responsável legal cadastrado. "
                "Cadastre o responsável antes de agendar o atendimento."
            )
            return

        try:
            self.__verifica_regra2(clinica, dados["hora_inicio"], dados["hora_fim"])
        except RegraNegocioException as e:
            self.__tela.mostra_mensagem(str(e))
            return

        try:
            novo = Atendimento(
                clinica=clinica,
                paciente=paciente,
                profissional=profissional,
                data=dados["data"],
                hora_inicio=dados["hora_inicio"],
                hora_fim=dados["hora_fim"],
                tipo=tipo,
                valor=dados["valor"]
            )
            self.__atendimentos.append(novo)
            self.__persistir()  # NOVO (Tarefa 2)
            self.__tela.mostra_mensagem("Atendimento cadastrado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_atendimento(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        self.listar_atendimentos()
        indice = self.__tela.seleciona_atendimento()
        atendimento = self.__buscar_por_indice(indice)
        if atendimento is None:
            self.__tela.mostra_mensagem("Atendimento não encontrado.")
            return

        ctrl_pagamento = self.__controlador_sistema.controlador_pagamento
        pagamentos = ctrl_pagamento.get_pagamentos()

        for pagamento in pagamentos:
            if pagamento.atendimento == atendimento:
                self.__tela.mostra_mensagem(
                    "Não é possível alterar este atendimento, pois já existe pagamento registrado para ele."
                )
                return

        dados = self.__tela.pega_dados_alteracao(atendimento)
        try:
            self.__verifica_regra2(atendimento.clinica, dados["hora_inicio"], dados["hora_fim"])
        except RegraNegocioException as e:
            self.__tela.mostra_mensagem(str(e))
            return

        try:
            atendimento.data        = dados["data"]
            atendimento.hora_inicio = dados["hora_inicio"]
            atendimento.hora_fim    = dados["hora_fim"]
            atendimento.valor       = dados["valor"]
            self.__persistir()  # NOVO (Tarefa 2)
            self.__tela.mostra_mensagem("Atendimento alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_atendimento(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        self.listar_atendimentos()
        indice = self.__tela.seleciona_atendimento()
        atendimento = self.__buscar_por_indice(indice)
        if atendimento is None:
            self.__tela.mostra_mensagem("Atendimento não encontrado.")
            return

        ctrl_pagamento = self.__controlador_sistema.controlador_pagamento
        pagamentos = ctrl_pagamento.get_pagamentos()

        for pagamento in pagamentos:
            if pagamento.atendimento == atendimento:
                self.__tela.mostra_mensagem(
                    "Não é possível excluir este atendimento, pois já existe pagamento registrado para ele."
                )
                return

        self.__atendimentos.remove(atendimento)
        self.__persistir()  # NOVO (Tarefa 2)
        self.__tela.mostra_mensagem("Atendimento removido com sucesso!")

    def registrar_procedimento(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        ctrl_catalogo = self.__controlador_sistema.controlador_catalogo_procedimento

        if not ctrl_catalogo.get_procedimentos():
            self.__tela.mostra_mensagem("Nenhum procedimento cadastrado no catálogo. Cadastre um procedimento antes.")
            return

        self.listar_atendimentos()
        indice = self.__tela.seleciona_atendimento()
        atendimento = self.__buscar_por_indice(indice)
        if atendimento is None:
            self.__tela.mostra_mensagem("Atendimento não encontrado.")
            return

        ctrl_catalogo.listar_procedimentos()
        id_proc = self.__tela.pega_id_procedimento()
        procedimento = ctrl_catalogo.buscar_por_id(id_proc)
        if procedimento is None:
            self.__tela.mostra_mensagem("Procedimento não encontrado no catálogo.")
            return

        atendimento.adicionar_procedimento(
            procedimento.descricao,
            procedimento.custo,
            atendimento.profissional
        )
        self.__persistir()  # NOVO (Tarefa 2)
        self.__tela.mostra_mensagem("Procedimento registrado no atendimento!")

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        for i, atendimento in enumerate(self.__atendimentos):
            self.__tela.mostra_lista_atendimento(i, atendimento)
        self.__tela.exibir_buffer_atendimentos()  # NOVO

    def exibir_buffer_atendimentos(self):
        """Exibe e limpa o buffer quando a listagem é standalone (sem seleção)."""
        if not self.__lista_buffer:
            return
        texto = '\n\n'.join(self.__lista_buffer)
        self.__lista_buffer.clear()
        sg.popup_scrolled(texto, title='Atendimentos Cadastrados')

    def __buscar_por_indice(self, indice: int):
        """Retorna o atendimento na posição informada, ou None."""
        if 0 <= indice < len(self.__atendimentos):
            return self.__atendimentos[indice]
        return None

    def get_atendimentos(self) -> list:
        return list(self.__atendimentos)

