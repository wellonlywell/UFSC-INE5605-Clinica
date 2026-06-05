from model.Atendimento import Atendimento
from view.tela_atendimento import TelaAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException


class ControladorAtendimento:
   
    def __init__(self, controlador_sistema):
        self.__atendimentos = []
        self.__tela = TelaAtendimento()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 1:
                self.incluir_atendimento()
            elif opcao == 2:
                self.alterar_atendimento()
            elif opcao == 3:
                self.listar_atendimentos()
            elif opcao == 4:
                self.excluir_atendimento()
            elif opcao == 0:
                break

    def incluir_atendimento(self):
        """
        Pede dados à tela, busca os objetos necessários nos outros
        controladores e cria um novo Atendimento.
        """
        dados = self.__tela.pega_dados_atendimento()

        # --- Busca os objetos nos respectivos controladores ---
        ctrl_clinica = self.__controlador_sistema.controlador_clinica
        ctrl_paciente = self.__controlador_sistema.controlador_paciente
        ctrl_profissional = self.__controlador_sistema.controlador_profissional
        ctrl_tipo = self.__controlador_sistema.controlador_tipo_atendimento

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

        # --- Regra 1: paciente deve ter 18 anos ou mais ---
        if not paciente.maior_de_idade and paciente.responsavel is None:
            self.__tela.mostra_mensagem(
                "Regra 1: Paciente menor de idade sem responsável. Cadastre um responsável."
            )
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
        dados = self.__tela.pega_dados_atendimento()
        try:
            atendimento.data = dados["data"]
            atendimento.hora_inicio = dados["hora_inicio"]
            atendimento.hora_fim = dados["hora_fim"]
            atendimento.valor = dados["valor"]
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
        self.__atendimentos.remove(atendimento)
        self.__tela.mostra_mensagem("Atendimento removido com sucesso!")

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        for i, atendimento in enumerate(self.__atendimentos):
            print(f"\n[{i}]")
            self.__tela.mostra_atendimento(atendimento)

    def __buscar_por_indice(self, indice: int):
        """Retorna o atendimento na posição informada, ou None."""
        if 0 <= indice < len(self.__atendimentos):
            return self.__atendimentos[indice]
        return None

    def get_atendimentos(self) -> list:
        return list(self.__atendimentos)
