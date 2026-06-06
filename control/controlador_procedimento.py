from model.Procedimento import Procedimento
from view.tela_procedimento import TelaProcedimento
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorProcedimento:

    def __init__(self, controlador_sistema):
        self.__procedimentos = []
        self.__tela_procedimento = TelaProcedimento()
        self.__controlador_sistema = controlador_sistema
        self.__proximo_id = 1

    def abre_tela(self):
        while True:
            opcao = self.__tela_procedimento.tela_opcoes()
            if opcao == 1:
                self.incluir_procedimento()
            elif opcao == 2:
                self.alterar_procedimento()
            elif opcao == 3:
                self.listar_procedimentos()
            elif opcao == 4:
                self.excluir_procedimento()
            elif opcao == 0:
                break

    def incluir_procedimento(self):
        ctrl_prof = self.__controlador_sistema.controlador_profissional
        if not ctrl_prof.get_profissionais():
            self.__tela_procedimento.mostra_mensagem(
                "Nenhum profissional cadastrado. Cadastre um profissional primeiro."
            )
            return
        dados = self.__tela_procedimento.pega_dados_procedimento()
        print("\n----- SELECIONAR PROFISSIONAL RESPONSÁVEL -----")
        ctrl_prof.listar_profissionais()
        cpf_prof = input("CPF do profissional responsável: ").strip()
        profissional = ctrl_prof.buscar_por_cpf(cpf_prof)
        if profissional is None:
            self.__tela_procedimento.mostra_mensagem("Profissional não encontrado.")
            return
        try:
            novo = Procedimento(
                id=self.__proximo_id,
                descricao=dados["descricao"],
                custo=dados["custo"],
                profissional=profissional
            )
            self.__procedimentos.append(novo)
            self.__proximo_id += 1
            self.__tela_procedimento.mostra_mensagem("Procedimento cadastrado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_procedimento.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_procedimento(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        self.listar_procedimentos()
        id_buscado = self.__tela_procedimento.seleciona_procedimento()
        procedimento = self.buscar_por_id(id_buscado)
        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem("Procedimento não encontrado.")
            return
        dados = self.__tela_procedimento.pega_dados_procedimento()
        try:
            procedimento.descricao = dados["descricao"]
            procedimento.custo = dados["custo"]
            self.__tela_procedimento.mostra_mensagem("Procedimento alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_procedimento.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_procedimento(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        self.listar_procedimentos()
        id_buscado = self.__tela_procedimento.seleciona_procedimento()
        procedimento = self.buscar_por_id(id_buscado)
        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem("Procedimento não encontrado.")
            return
        self.__procedimentos.remove(procedimento)
        self.__tela_procedimento.mostra_mensagem("Procedimento removido com sucesso!")

    def listar_procedimentos(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        for procedimento in self.__procedimentos:
            self.__tela_procedimento.mostra_procedimento(procedimento)

    def buscar_por_id(self, id: int):
        for procedimento in self.__procedimentos:
            if procedimento.id == id:
                return procedimento
        return None

    def get_procedimentos(self) -> list:
        return list(self.__procedimentos)