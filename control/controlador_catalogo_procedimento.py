from model.CatalogoProcedimento import CatalogoProcedimento
from view.tela_catalogo_procedimento import TelaCatalogoProcedimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException
from dao.dao_catalogo_procedimento import CatalogoProcedimentoDAO  # T2: DAO do catálogo

class ControladorCatalogoProcedimento:

    def __init__(self, controlador_sistema):
        self.__dao = CatalogoProcedimentoDAO()  # T2: cria o DAO
        self.__procedimentos = self.__dao.get_all()  # T2: carrega do disco
        self.__tela_procedimento = TelaCatalogoProcedimento()
        self.__controlador_sistema = controlador_sistema
        # T2: recalcula o próximo ID a partir do que já foi carregado,
        # senão reinicia em 1 e repete ID depois de reabrir o sistema
        self.__proximo_id = max((p.id for p in self.__procedimentos), default=0) + 1

    def __persistir(self):  # T2: salva a lista em disco
        self.__dao.save_all(self.__procedimentos)

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_procedimento.tela_opcoes()
                if opcao == 1: self.incluir_procedimento()
                elif opcao == 2: self.alterar_procedimento()
                elif opcao == 3: self.listar_procedimentos()
                elif opcao == 4: self.excluir_procedimento()
                elif opcao == 0: break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela_procedimento.mostra_mensagem(str(e))

    def incluir_procedimento(self):
        dados = self.__tela_procedimento.pega_dados_procedimento()

        if self.buscar_por_descricao(dados["descricao"]):
            raise RegraNegocioException("Já existe um procedimento com esta descrição.")

        novo = CatalogoProcedimento(
            id=self.__proximo_id,
            descricao=dados["descricao"],
            custo=dados["custo"]
        )
        self.__procedimentos.append(novo)
        self.__proximo_id += 1
        self.__persistir()  # T2: grava no disco
        self.__tela_procedimento.mostra_mensagem("Procedimento cadastrado com sucesso!")

    def alterar_procedimento(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        
        self.listar_procedimentos()
        id_buscado = self.__tela_procedimento.seleciona_procedimento()
        if id_buscado == 0: return # Rota de fuga

        procedimento = self.buscar_por_id(id_buscado)
        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem(f"Erro: Não existe procedimento com o ID {id_buscado}.")
            return
        
        dados = self.__tela_procedimento.pega_dados_procedimento()

        procedimento_existente = self.buscar_por_descricao(dados["descricao"])
        if procedimento_existente and procedimento_existente.id != procedimento.id:
            self.__tela_procedimento.mostra_mensagem("Erro: Já existe outro procedimento com esta descrição no catálogo.")
            return

        try:
            procedimento.descricao = dados["descricao"]
            procedimento.custo = dados["custo"]
            self.__persistir()  # T2: grava no disco
            self.__tela_procedimento.mostra_mensagem("Procedimento alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_procedimento.mostra_mensagem(f"Erro nos dados: {e}")
          
        
    def excluir_procedimento(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
            
        self.listar_procedimentos()
        id_buscado = self.__tela_procedimento.seleciona_procedimento()
        if id_buscado == 0: return # Rota de fuga

        procedimento = self.buscar_por_id(id_buscado)
        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem(f"Erro: Não existe procedimento com o ID {id_buscado}.")
            return
        
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        for at in atendimentos:
            for item in at.procedimentos:
                if item.descricao.lower() == procedimento.descricao.lower():
                    self.__tela_procedimento.mostra_mensagem(
                        f"Não é possível excluir '{procedimento.descricao}': "
                        f"já foi usado em um atendimento."
                    )
                    return
                    
        self.__procedimentos.remove(procedimento)
        self.__dao.save_all(self.__procedimentos)  # T2: grava no disco
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

    def buscar_por_descricao(self, descricao):
        for proc in self.__procedimentos:
            if proc.descricao.lower() == descricao.lower():
                return proc
        return None

    def get_procedimentos(self) -> list:
        return list(self.__procedimentos)