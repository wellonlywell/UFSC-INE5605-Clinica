class TelaPessoa():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PESSOAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Pessoa")
    print("2 - Alterar Pessoa")
    print("3 - Listar Pessoas")
    print("4 - Excluir Pessoa")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
 pass
