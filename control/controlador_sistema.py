# Controlador Principal do Sistemaclass TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisClinica ---------")
        print("Escolha sua opcao")
        print("1 - Clínica")
        print("2 - Atendimento")
        print("3 - Pagamento")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao