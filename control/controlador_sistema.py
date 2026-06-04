
class ControladorSistema:
    
    def __init__(self):
        
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)
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
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()

            if opcao == 1:
                self.__controlador_paciente.abre_tela()
            elif opcao == 2:
                self.__controlador_profissional.abre_tela()
            elif opcao == 3:
                self.__controlador_clinica.abre_tela()
            elif opcao == 4:
                self.__controlador_tipo_atendimento.abre_tela()
            elif opcao == 5:
                self.__controlador_atendimento.abre_tela()
            elif opcao == 6:
                self.__controlador_pagamento.abre_tela()
            elif opcao == 0:
                self.__tela_sistema.mostra_mensagem("Sistema encerrado. Até logo!")
                break