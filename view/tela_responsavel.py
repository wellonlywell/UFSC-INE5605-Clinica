class TelaResponsavel():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- RESPONSÁVEIS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Responsável")
    print("2 - Alterar Responsável")
    print("3 - Listar Responsáveis")
    print("4 - Excluir Responsável")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
