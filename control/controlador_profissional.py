from model.Profissional import Profissional
from model.CorRaca import CorRaca
from view.tela_profissional import TelaProfissional
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorProfissional:

    def __init__(self, controlador_sistema):
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela_profissional.tela_opcoes()
            if opcao == 1:
                self.incluir_profissional()
            elif opcao == 2:
                self.alterar_profissional()
            elif opcao == 3:
                self.listar_profissionais()
            elif opcao == 4:
                self.excluir_profissional()
            elif opcao == 0:
                break

    def incluir_profissional(self):
        dados = self.__tela_profissional.pega_dados_profissional()
        try:
            if self.buscar_por_cpf(dados["cpf"]) is not None:
                self.__tela_profissional.mostra_mensagem("Já existe um profissional com este CPF.")
                return
            cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
            novo = Profissional(
                nome_civil=dados["nome_civil"],
                celular=dados["celular"],
                cpf=dados["cpf"],
                especialidade=dados["especialidade"],
                registro=dados["registro"],
                nome_social=dados["nome_social"],
                pcd=dados["pcd"],
                cor_raca=cor_raca,
                identidade_genero=dados["identidade_genero"]
            )
            self.__profissionais.append(novo)
            self.__tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_profissional.mostra_mensagem(f"Erro nos dados: {e}")

    def alterar_profissional(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        self.listar_profissionais()
        cpf = self.__tela_profissional.seleciona_profissional()
        profissional = self.buscar_por_cpf(cpf)
        if profissional is None:
            self.__tela_profissional.mostra_mensagem("Profissional não encontrado.")
            return
        dados = self.__tela_profissional.pega_dados_profissional()
        try:
            cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
            profissional.nome_civil = dados["nome_civil"]
            profissional.nome_social = dados["nome_social"]
            profissional.celular = dados["celular"]
            profissional.especialidade = dados["especialidade"]
            profissional.registro = dados["registro"]
            profissional.pcd = dados["pcd"]
            profissional.cor_raca = cor_raca
            profissional.identidade_genero = dados["identidade_genero"]
            self.__tela_profissional.mostra_mensagem("Profissional alterado com sucesso!")
        except DadoInvalidoException as e:
            self.__tela_profissional.mostra_mensagem(f"Erro nos dados: {e}")

    def excluir_profissional(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        self.listar_profissionais()
        cpf = self.__tela_profissional.seleciona_profissional()
        profissional = self.buscar_por_cpf(cpf)
        if profissional is None:
            self.__tela_profissional.mostra_mensagem("Profissional não encontrado.")
            return
        self.__profissionais.remove(profissional)
        self.__tela_profissional.mostra_mensagem("Profissional removido com sucesso!")

    def listar_profissionais(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        for profissional in self.__profissionais:
            self.__tela_profissional.mostra_profissional(profissional)

    def buscar_por_cpf(self, cpf: str):
        digitos = "".join(c for c in cpf if c.isdigit())
        for profissional in self.__profissionais:
            if "".join(c for c in profissional.cpf if c.isdigit()) == digitos:
                return profissional
        return None

    def get_profissionais(self) -> list:
        return list(self.__profissionais)

    def __converter_cor_raca(self, opcao: str):
        mapa = {
            "1": CorRaca.BRANCA, "2": CorRaca.PRETA, "3": CorRaca.PARDA,
            "4": CorRaca.AMARELA, "5": CorRaca.INDIGENA, "6": CorRaca.NAO_INFORMADO
        }
        return mapa.get(opcao, CorRaca.NAO_INFORMADO)