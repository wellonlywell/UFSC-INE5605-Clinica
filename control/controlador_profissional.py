from model.Profissional import Profissional
from model.CorRaca import CorRaca
from view.tela_profissional import TelaProfissional
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.regra_negocio_exception import RegraNegocioException
from dao.dao_profissional import ProfissionalDAO  # T2: DAO do profissional

class ControladorProfissional:

    def __init__(self, controlador_sistema):
        self.__dao = ProfissionalDAO()  # T2: cria o DAO
        self.__profissionais = self.__dao.get_all()  # T2: carrega do disco
        self.__tela_profissional = TelaProfissional()
        self.__controlador_sistema = controlador_sistema

    def __persistir(self):  # T2: salva a lista em disco
        self.__dao.save_all(self.__profissionais)

    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_profissional.tela_opcoes()
                if opcao == 1: self.incluir_profissional()
                elif opcao == 2: self.alterar_profissional()
                elif opcao == 3: self.listar_profissionais()
                elif opcao == 4: self.excluir_profissional()
                elif opcao == 0: break
            except (DadoInvalidoException, RegraNegocioException) as e:
                self.__tela_profissional.mostra_mensagem(str(e))

    def incluir_profissional(self):
        dados = self.__tela_profissional.pega_dados_profissional()
        if self.buscar_por_cpf(dados["cpf"]) is not None:
            raise RegraNegocioException("Já existe um profissional cadastrado com este CPF.")
            
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
        self.__persistir()  # T2: grava no disco
        self.__tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")
    
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
        
        cor_raca = self.__converter_cor_raca(dados["cor_raca_opcao"])
        profissional.nome_civil = dados["nome_civil"]
        profissional.nome_social = dados["nome_social"]
        profissional.celular = dados["celular"]
        profissional.especialidade = dados["especialidade"]
        profissional.registro = dados["registro"]
        profissional.pcd = dados["pcd"]
        profissional.cor_raca = cor_raca
        profissional.identidade_genero = dados["identidade_genero"]
        
        self.__persistir()  # T2: grava no disco
        self.__tela_profissional.mostra_mensagem("Profissional alterado com sucesso!")

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
        
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()

        for atendimento in atendimentos:
            if atendimento.profissional.cpf == profissional.cpf: # T2: compara por CPF, não por identidade do objeto
                self.__tela_profissional.mostra_mensagem(
                    "Não é possível excluir este profissional, pois ele já possui atendimento registrado."
                )
                return
            
        self.__profissionais.remove(profissional)
        self.__persistir()  # T2: grava no disco
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
