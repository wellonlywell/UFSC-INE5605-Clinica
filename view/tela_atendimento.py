class TelaAtendimento():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ATENDIMENTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Atendimento")
    print("2 - Alterar Atendimento")
    print("3 - Listar Atendimentos")
    print("4 - Excluir Atendimento")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass