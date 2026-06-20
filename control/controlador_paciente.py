from model.Paciente import Paciente
from model.Responsavel import Responsavel
from model.CorRaca import CorRaca
from view.tela_paciente import TelaPaciente
from view.tela_responsavel import TelaResponsavel
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException


class ControladorPaciente:

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__tela_responsavel = TelaResponsavel()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_paciente.tela_opcoes()
                if opcao == 1:
                    self.incluir_paciente()
                elif opcao == 2:
                    self.alterar_paciente()
                elif opcao == 3:
                    self.listar_pacientes()
                elif opcao == 4:
                    self.excluir_paciente()
                elif opcao == 0:
                    break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela_paciente.mostra_mensagem(str(e))

    def incluir_paciente(self):
        
        dados = self.__tela_paciente.pega_dados_paciente()

        if self.buscar_por_cpf(dados["cpf"]) is not None:
            self.__tela_paciente.mostra_mensagem("Já existe um paciente com este CPF.")
            return

        cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])

        try:
            novo = Paciente(
                nome_civil=dados["nome_civil"],
                celular=dados["celular"],
                cpf=dados["cpf"],
                data_nascimento=dados["data_nascimento"],
                nome_social=dados["nome_social"],
                pcd=dados["pcd"],
                cor_raca=cor_raca,
                identidade_genero=dados["identidade_genero"]
            )
        except DadoInvalidoException as e:
            self.__tela_paciente.mostra_mensagem(f"Erro nos dados: {e}")
            return
        
        if not novo.maior_de_idade:
            self.__tela_paciente.mostra_mensagem(
                f"Paciente tem {novo.idade} anos (menor de idade). "
                "É obrigatório cadastrar um responsável legal."
            )
            responsavel = self.__cadastrar_responsavel()
            if responsavel is None:
                self.__tela_paciente.mostra_mensagem(
                    "Cadastro cancelado: responsável é obrigatório para menores de 18 anos."
                )
                return
            novo.responsavel = responsavel

        self.__pacientes.append(novo)
        self.__tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")

    def __cadastrar_responsavel(self):
        
        try:
            dados = self.__tela_responsavel.pega_dados_responsavel()
            cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
            responsavel = Responsavel(
                nome_civil=dados["nome_civil"],
                celular=dados["celular"],
                cpf=dados["cpf"],
                parentesco=dados["parentesco"],
                nome_social=dados["nome_social"],
                pcd=dados["pcd"],
                cor_raca=cor_raca,
                identidade_genero=dados["identidade_genero"]
            )
            self.__controlador_sistema.controlador_responsavel.registrar_responsavel(responsavel)
            return responsavel
        except (DadoInvalidoException, RegraNegocioException) as e:
            self.__tela_paciente.mostra_mensagem(f"Erro nos dados do responsável: {e}")
            return None

    def alterar_paciente(self):
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        self.listar_pacientes()
        cpf = self.__tela_paciente.seleciona_paciente()
        paciente = self.buscar_por_cpf(cpf)
        if paciente is None:
            self.__tela_paciente.mostra_mensagem("Paciente não encontrado.")
            return
        dados = self.__tela_paciente.pega_dados_paciente()
        try:
            cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
            paciente.nome_civil         = dados["nome_civil"]
            paciente.nome_social        = dados["nome_social"]
            paciente.celular            = dados["celular"]
            paciente.data_nascimento    = dados["data_nascimento"]
            paciente.pcd                = dados["pcd"]
            paciente.cor_raca           = cor_raca
            paciente.identidade_genero  = dados["identidade_genero"]
            self.__tela_paciente.mostra_mensagem("Paciente alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_paciente.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_paciente(self):
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        self.listar_pacientes()
        cpf = self.__tela_paciente.seleciona_paciente()
        paciente = self.buscar_por_cpf(cpf)
        if paciente is None:
            self.__tela_paciente.mostra_mensagem("Paciente não encontrado.")
            return
        self.__pacientes.remove(paciente)
        self.__tela_paciente.mostra_mensagem("Paciente removido com sucesso!")

    def listar_pacientes(self):
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_paciente(paciente)

    def buscar_por_cpf(self, cpf: str):
        digitos = "".join(c for c in cpf if c.isdigit())
        for paciente in self.__pacientes:
            if "".join(c for c in paciente.cpf if c.isdigit()) == digitos:
                return paciente
        return None

    def get_pacientes(self) -> list:
        return list(self.__pacientes)

    def __converter_cor_raca(self, opcao: str):
        mapa = {
            "1": CorRaca.BRANCA,  "2": CorRaca.PRETA,
            "3": CorRaca.PARDA,   "4": CorRaca.AMARELA,
            "5": CorRaca.INDIGENA, "6": CorRaca.NAO_INFORMADO
        }
        return mapa.get(opcao, CorRaca.NAO_INFORMADO)
