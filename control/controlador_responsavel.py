from model.Responsavel import Responsavel
from model.CorRaca import CorRaca
from view.tela_responsavel import TelaResponsavel
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException

class ControladorResponsavel:

    def __init__(self, controlador_sistema):
        self.__responsaveis = []
        self.__tela_responsavel = TelaResponsavel()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_responsavel.tela_opcoes()
                if opcao == 1: self.incluir_responsavel()
                elif opcao == 2: self.alterar_responsavel()
                elif opcao == 3: self.listar_responsaveis()
                elif opcao == 4: self.excluir_responsavel()
                elif opcao == 0: break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela_responsavel.mostra_mensagem(str(e))

    def registrar_responsavel(self, responsavel):
        self.__responsaveis.append(responsavel)

    def incluir_responsavel(self):
        dados = self.__tela_responsavel.pega_dados_responsavel()
        
        if self.buscar_por_cpf(dados["cpf"]) is not None:
            raise RegraNegocioException("Já existe um responsável cadastrado com este CPF.")
            
        cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
        novo = Responsavel(
            nome_civil=dados["nome_civil"],
            celular=dados["celular"],
            cpf=dados["cpf"],
            parentesco=dados["parentesco"],
            nome_social=dados["nome_social"],
            pcd=dados["pcd"],
            cor_raca=cor_raca,
            identidade_genero=dados["identidade_genero"]
        )
        self.__responsaveis.append(novo)
        self.__tela_responsavel.mostra_mensagem("Responsável cadastrado com sucesso!")

    def alterar_responsavel(self):
        if not self.__responsaveis:
            self.__tela_responsavel.mostra_mensagem("Nenhum responsável cadastrado.")
            return
        self.listar_responsaveis()
        cpf = self.__tela_responsavel.seleciona_responsavel()
        responsavel = self.buscar_por_cpf(cpf)
        if responsavel is None:
            self.__tela_responsavel.mostra_mensagem("Responsável não encontrado.")
            return
            
        dados = self.__tela_responsavel.pega_dados_responsavel()
        
        cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
        responsavel.nome_civil = dados["nome_civil"]
        responsavel.nome_social = dados["nome_social"]
        responsavel.celular = dados["celular"]
        responsavel.parentesco = dados["parentesco"]
        responsavel.pcd = dados["pcd"]
        responsavel.cor_raca = cor_raca
        responsavel.identidade_genero = dados["identidade_genero"]
        
        self.__tela_responsavel.mostra_mensagem("Responsável alterado com sucesso!")

    def excluir_responsavel(self):
        if not self.__responsaveis:
            self.__tela_responsavel.mostra_mensagem("Nenhum responsável cadastrado.")
            return
        self.listar_responsaveis()
        cpf = self.__tela_responsavel.seleciona_responsavel()
        responsavel = self.buscar_por_cpf(cpf)
        if responsavel is None:
            self.__tela_responsavel.mostra_mensagem("Responsável não encontrado.")
            return
        self.__responsaveis.remove(responsavel)
        self.__tela_responsavel.mostra_mensagem("Responsável removido com sucesso!")

    def listar_responsaveis(self):
        if not self.__responsaveis:
            self.__tela_responsavel.mostra_mensagem("Nenhum responsável cadastrado.")
            return
        for responsavel in self.__responsaveis:
            self.__tela_responsavel.mostra_responsavel(responsavel)

    def buscar_por_cpf(self, cpf: str):
        digitos = "".join(c for c in cpf if c.isdigit())
        for responsavel in self.__responsaveis:
            if "".join(c for c in responsavel.cpf if c.isdigit()) == digitos:
                return responsavel
        return None

    def get_responsaveis(self) -> list:
        return list(self.__responsaveis)

    def __converter_cor_raca(self, opcao: str):
        mapa = {
            "1": CorRaca.BRANCA, "2": CorRaca.PRETA, "3": CorRaca.PARDA,
            "4": CorRaca.AMARELA, "5": CorRaca.INDIGENA, "6": CorRaca.NAO_INFORMADO
        }
        return mapa.get(opcao, CorRaca.NAO_INFORMADO)