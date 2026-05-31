class TelaProcedimento():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PROCEDIMENTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Procedimento")
    print("2 - Alterar Procedimento")
    print("3 - Listar Procedimentos")
    print("4 - Excluir Procedimento")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass
