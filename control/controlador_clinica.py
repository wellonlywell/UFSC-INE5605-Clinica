from model.Clinica import Clinica
from view.tela_clinica import TelaClinica
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorClinica:

    def __init__(self, controlador_sistema):
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela_clinica.tela_opcoes()

            if opcao == 1:
                self.incluir_clinica()
            elif opcao == 2:
                self.alterar_clinica()
            elif opcao == 3:
                self.listar_clinicas()
            elif opcao == 4:
                self.excluir_clinica()
            elif opcao == 0:
                # Sai do loop e retorna para o menu principal
                break        

    def incluir_clinica(self):
        """Pede dados à tela, cria o objeto Clinica e adiciona na lista."""
        dados = self.__tela_clinica.pega_dados_clinica()
        try:
            nova_clinica = Clinica(
                nome=dados["nome"],
                cnpj=dados["cnpj"],
                cidade=dados["cidade"],
                descricao=dados["descricao"],
                horario_abertura=dados["horario_abertura"],
                horario_fechamento=dados["horario_fechamento"]
            )
            # Verifica se já existe uma clínica com o mesmo CNPJ
            if self.buscar_por_cnpj(dados["cnpj"]) is not None:
                self.__tela_clinica.mostra_mensagem("Já existe uma clínica com este CNPJ.")
                return
            self.__clinicas.append(nova_clinica)
            self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_clinica.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_clinica(self):
        """Busca uma clínica pelo CNPJ e atualiza seus dados."""
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        self.listar_clinicas()
        cnpj = self.__tela_clinica.seleciona_clinica()
        clinica = self.buscar_por_cnpj(cnpj)
        if clinica is None:
            self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
            return
        dados = self.__tela_clinica.pega_dados_clinica()
        try:
            clinica.nome = dados["nome"]
            clinica.cidade = dados["cidade"]
            # CNPJ não é alterado — é o identificador único
            self.__tela_clinica.mostra_mensagem("Clínica alterada com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_clinica.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_clinica(self):
        """Remove uma clínica da lista pelo CNPJ."""
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        self.listar_clinicas()
        cnpj = self.__tela_clinica.seleciona_clinica()
        clinica = self.buscar_por_cnpj(cnpj)
        if clinica is None:
            self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
            return
        self.__clinicas.remove(clinica)
        self.__tela_clinica.mostra_mensagem("Clínica removida com sucesso!")

    def listar_clinicas(self):
        """Exibe todas as clínicas cadastradas."""
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        for clinica in self.__clinicas:
            self.__tela_clinica.mostra_clinica(clinica)

    def buscar_por_cnpj(self, cnpj: str):
        
        digitos_buscados = "".join(c for c in cnpj if c.isdigit())
        for clinica in self.__clinicas:
            digitos_clinica = "".join(c for c in clinica.cnpj if c.isdigit())
            if digitos_clinica == digitos_buscados:
                return clinica
        return None

    def get_clinicas(self) -> list:
        """Retorna cópia da lista de clínicas (para uso de outros controladores)."""
        return list(self.__clinicas)
