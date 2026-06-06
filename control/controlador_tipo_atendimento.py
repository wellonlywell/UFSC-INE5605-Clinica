from model.TipoAtendimento import TipoAtendimento
from view.tela_tipo_atendimento import TelaTipoAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException

class ControladorTipoAtendimento():

  def __init__(self, controlador_sistema):
    self.__tipos_atendimento = []
    self.__tela_tipo_atendimento = TelaTipoAtendimento()
    self.__controlador_sistema = controlador_sistema

pass