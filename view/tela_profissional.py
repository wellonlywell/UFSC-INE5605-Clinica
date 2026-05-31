class TelaProfissional():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PROFISSIONAIS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Profissional")
    print("2 - Alterar Profissional")
    print("3 - Listar Profissionais")
    print("4 - Excluir Profissional")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass