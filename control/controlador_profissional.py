from model.Profissional import Profissional
from model.CorRaca import CorRaca
from view.tela_profissional import TelaProfissional
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorProfissional():

  def __init__(self, controlador_sistema):
    self.__profissionais = []
    self.__tela_profissional = TelaProfissional()
    self.__controlador_sistema = controlador_sistema
pass
