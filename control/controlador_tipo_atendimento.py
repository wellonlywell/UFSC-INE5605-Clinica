from model.TipoAtendimento import TipoAtendimento
from view.tela_tipo_atendimento import TelaTipoAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from dao.dao_tipo_atendimento import TipoAtendimentoDAO  # NOVO (Tarefa 2)


class ControladorTipoAtendimento:

    def __init__(self, controlador_sistema):
        self.__dao = TipoAtendimentoDAO()  # NOVO (Tarefa 2)
        self.__tipos_atendimento = self.__dao.get_all()  # ALTERADO: antes era [] (Tarefa 2)
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__controlador_sistema = controlador_sistema
        # ALTERADO (Tarefa 2): recalcula o próximo ID a partir dos dados
        # carregados, em vez de sempre iniciar em 1, evitando colisão de
        # IDs com tipos de atendimento já persistidos.
        self.__proximo_id = self.__calcular_proximo_id()

    def __calcular_proximo_id(self) -> int:
        """Retorna o próximo ID livre, com base no maior ID já carregado. (Tarefa 2)"""
        if not self.__tipos_atendimento:
            return 1
        return max(tipo.id for tipo in self.__tipos_atendimento) + 1

    def __persistir(self):
        """Grava o estado atual da lista de tipos de atendimento em disco. (Tarefa 2)"""
        self.__dao.save_all(self.__tipos_atendimento)

    def abre_tela(self):
        while True:
            opcao = self.__tela_tipo_atendimento.tela_opcoes()
            if opcao == 1:
                self.incluir_tipo_atendimento()
            elif opcao == 2:
                self.alterar_tipo_atendimento()
            elif opcao == 3:
                self.listar_tipos_atendimento()
            elif opcao == 4:
                self.excluir_tipo_atendimento()
            elif opcao == 0:
                break

    def incluir_tipo_atendimento(self):
        dados = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()
        if dados["descricao"].isdigit():
            self.__tela_tipo_atendimento.mostra_mensagem("Descrição inválida: não pode ser apenas números.")
            return
        try:
            novo = TipoAtendimento(id=self.__proximo_id, descricao=dados["descricao"])
            self.__tipos_atendimento.append(novo)
            self.__proximo_id += 1
            self.__persistir()  # NOVO (Tarefa 2)
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_tipo_atendimento.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        self.listar_tipos_atendimento()
        id_buscado = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()

        if id_buscado == 0:
            self.__tela_tipo_atendimento.mostra_mensagem("Operação cancelada. Retornando ao menu...")
            return

        tipo = self.buscar_por_id(id_buscado)
        if tipo is None:
            self.__tela_tipo_atendimento.mostra_mensagem(f"O ID {id_buscado} não foi encontrado no sistema.")
            return
        dados = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento("ALTERAR", tipo)
        if dados["descricao"].isdigit():
            self.__tela_tipo_atendimento.mostra_mensagem("Descrição inválida: não pode ser apenas números.")
            return
        try:
            tipo.descricao = dados["descricao"]
            self.__persistir()  # NOVO (Tarefa 2)
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_tipo_atendimento.mostra_mensagem(f"Erro nos dados: {e}")

    def listar_tipos_atendimento(self):
        if not self.__tipos_atendimento: # caso não tenha nenhum tipo cadastrado, ele avisa e retorna
            self.__tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        for tipo in self.__tipos_atendimento: # caso já tenha tipos cadastrados, ele mostra a lista completa
            self.__tela_tipo_atendimento.mostra_tipo_atendimento(tipo)

    def buscar_por_id(self, id: int):
        for tipo in self.__tipos_atendimento:
            if tipo.id == id:
                return tipo
        return None

    def buscar_por_descricao(self, descricao: str):
        for tipo in self.__tipos_atendimento:
            if tipo.descricao.lower() == descricao.lower():
                return tipo
        return None

    def excluir_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        self.listar_tipos_atendimento()
        id_buscado = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()

        if id_buscado == 0:
            self.__tela_tipo_atendimento.mostra_mensagem("Operação cancelada. Retornando ao menu...")
            return

        tipo = self.buscar_por_id(id_buscado)
        if tipo is None:
            self.__tela_tipo_atendimento.mostra_mensagem(f"O ID {id_buscado} não foi encontrado no sistema.")
            return

        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()

        for atendimento in atendimentos:
            if atendimento.tipo == tipo:
                self.__tela_tipo_atendimento.mostra_mensagem(
                    "Não é possível excluir este tipo de atendimento, pois ele já foi usado em atendimento."
                )
                return

        self.__tipos_atendimento.remove(tipo)
        self.__persistir()  # NOVO (Tarefa 2)
        self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento removido com sucesso!")

    def get_tipos_atendimento(self) -> list:
        return list(self.__tipos_atendimento)

