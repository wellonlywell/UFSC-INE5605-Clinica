class TelaPaciente():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PACIENTES ----------")
    print("Escolha a opcao")
    print("1 - Incluir Paciente")
    print("2 - Alterar Paciente")
    print("3 - Listar Pacientes")
    print("4 - Excluir Paciente")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass