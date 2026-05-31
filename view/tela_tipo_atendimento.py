class TelaTipoAtendimento():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- TIPOS DE ATENDIMENTO ----------")
    print("Escolha a opcao")
    print("1 - Incluir Tipo de Atendimento")
    print("2 - Alterar Tipo de Atendimento")
    print("3 - Listar Tipos de Atendimento")
    print("4 - Excluir Tipo de Atendimento")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass