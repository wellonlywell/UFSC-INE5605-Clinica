class TelaCorRaca():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- COR/RACA ----------")
    print("Escolha a opcao")
    print("1 - Incluir Cor/Raca")
    print("2 - Alterar Cor/Raca")
    print("3 - Listar Cores/Racas")
    print("4 - Excluir Cor/Raca")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass