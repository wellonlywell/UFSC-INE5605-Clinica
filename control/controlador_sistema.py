from control.controlador_clinica import ControladorClinica
from control.controlador_paciente import ControladorPaciente
from control.controlador_profissional import ControladorProfissional
from control.controlador_tipo_atendimento import ControladorTipoAtendimento
from control.controlador_procedimento import ControladorProcedimento
from control.controlador_atendimento import ControladorAtendimento
from control.controlador_pagamento import ControladorPagamento
from control.controlador_relatorios import ControladorRelatorios
from control.controlador_responsavel import ControladorResponsavel
from view.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_procedimento = ControladorProcedimento(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_relatorios = ControladorRelatorios(self)
        self.__controlador_responsavel = ControladorResponsavel(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento

    @property
    def controlador_procedimento(self):
        return self.__controlador_procedimento

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios

    @property
    def controlador_responsavel(self):
        return self.__controlador_responsavel

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()

            if opcao == 1:
                self.__controlador_clinica.abre_tela()
            elif opcao == 2:
                self.__controlador_profissional.abre_tela()
            elif opcao == 3:
                self.__controlador_tipo_atendimento.abre_tela()
            elif opcao == 4:
                self.__controlador_procedimento.abre_tela()
            elif opcao == 5:
                self.__controlador_paciente.abre_tela()
            elif opcao == 6:
                self.__controlador_atendimento.abre_tela()
            elif opcao == 7:
                self.__controlador_pagamento.abre_tela()
            elif opcao == 8:
                self.__controlador_relatorios.abre_tela()
            elif opcao == 0:
                self.__tela_sistema.mostra_mensagem("Sistema encerrado. Até logo!")
                break
            