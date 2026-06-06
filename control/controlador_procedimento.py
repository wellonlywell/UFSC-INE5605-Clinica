from model.Procedimento import Procedimento
from view.tela_procedimento import TelaProcedimento
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorProcedimento():

  def __init__(self, controlador_sistema):
    self.__procedimentos = []
    self.__tela_procedimento = TelaProcedimento()
    self.__controlador_sistema = controlador_sistema
pass