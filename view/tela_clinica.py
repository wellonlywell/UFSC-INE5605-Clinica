class TelaClinica():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CLINICA ----------")
    print("Escolha a opcao")
    print("1 - Incluir Clinica")
    print("2 - Alterar Clinica")
    print("3 - Listar Clinicas")
    print("4 - Excluir Clinica")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass