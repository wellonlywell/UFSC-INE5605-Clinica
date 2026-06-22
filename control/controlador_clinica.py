from model.Clinica import Clinica
from view.tela_clinica import TelaClinica
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException


class ControladorClinica:

    def __init__(self, controlador_sistema):
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            try:
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
                    break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela_clinica.mostra_mensagem(str(e))

    def incluir_clinica(self):
        dados = self.__tela_clinica.pega_dados_clinica()
        try:
            if self.buscar_por_cnpj(dados["cnpj"]) is not None:
                self.__tela_clinica.mostra_mensagem("Já existe uma clínica com este CNPJ.")
                return
            nova_clinica = Clinica(
                nome=dados["nome"],
                cnpj=dados["cnpj"],
                cidade=dados["cidade"],
                descricao=dados["descricao"],
                horario_abertura=dados["horario_abertura"],
                horario_fechamento=dados["horario_fechamento"]
            )
            self.__clinicas.append(nova_clinica)
            self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_clinica.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_clinica(self):
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
            clinica.descricao = dados["descricao"]
            clinica.horario_abertura = dados["horario_abertura"]
            clinica.horario_fechamento = dados["horario_fechamento"]
            self.__tela_clinica.mostra_mensagem("Clínica alterada com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_clinica.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_clinica(self):
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        self.listar_clinicas()
        cnpj = self.__tela_clinica.seleciona_clinica()
        clinica = self.buscar_por_cnpj(cnpj)
        if clinica is None:
            self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
            return

        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        total_vinculados = 0
        for at in atendimentos:
            if at.clinica is clinica:
                total_vinculados += 1
        if total_vinculados > 0:
            self.__tela_clinica.mostra_mensagem(
                f"Não é possível excluir: {total_vinculados} atendimento(s) "
                "referencia(m) esta clínica."
            )
            return 

        self.__clinicas.remove(clinica)
        self.__tela_clinica.mostra_mensagem("Clínica removida com sucesso!")

    def listar_clinicas(self):
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
        return list(self.__clinicas)