
class TelaSistema:
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    """Mostra o menu principal do SisClínica."""
    print("-------- SisClínica ---------")
    print("1 - Gerenciar Pacientes")
    print("2 - Gerenciar Responsáveis")
    print("3 - Gerenciar Profissionais de Saúde")
    print("4 - Gerenciar Tipos de Atendimento")
    print("5 - Gerenciar Procedimentos")
    print("6 - Gerenciar Agendamentos / Consultas")
    print("7 - Relatórios e Indicadores")
    print("8 - Configurações da Clínica")
    print("0 - Sair do SisTema")
    print("-----------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
          return opcao
        print("Opção inválida! Digite um número correspondente ao menu.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def mostra_mensagem(self, mensagem: str):
    """Mostra mensagens gerais do sistema."""
    print(f"\n[Sistema]: {mensagem}")