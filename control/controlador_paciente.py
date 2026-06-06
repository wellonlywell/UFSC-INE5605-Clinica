from model.Paciente import Paciente
from model.CorRaca import CorRaca
from view.tela_paciente import TelaPaciente
from exceptions.dado_invalido_exception import DadoInvalidoException

class ControladorPaciente():

  def __init__(self, controlador_sistema):
    self.__paciente = []
    self.__tela_paciente = TelaPaciente()
    self.__controlador_sistema = controlador_sistema
pass