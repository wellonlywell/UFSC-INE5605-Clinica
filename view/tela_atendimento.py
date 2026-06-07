# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

class TelaAtendimento:
  def tela_opcoes(self):
    """Mostra o menu de gerenciamento de consultas/atendimentos."""
    print("-------- MENU AGENDAMENTOS/ATENDIMENTOS ----------")
    print("1 - Agendar Novo Atendimento")
    print("2 - Alterar Data/Hora de Agendamento")
    print("3 - Listar Todos os Atendimentos")
    print("4 - Cancelar Atendimento")
    print("5 - Iniciar/Finalizar Atendimento na SisClínica")
    print("0 - Retornar ao Menu Principal")
    print("--------------------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4, 5]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 5.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_atendimento(self):
    """Pede os identificadores essenciais para criar a agenda."""
    print("\n----- INSERIR DADOS DO AGENDAMENTO -----")
    cpf_paciente = input("CPF do Paciente (apenas números): ").strip()
    cpf_profissional = input("CPF do Profissional de Saúde (apenas números): ").strip()
    codigo_tipo = input("Código do Tipo de Atendimento: ").strip().upper()
    data_hora = input("Data e Hora do Atendimento (DD/MM/AAAA HH:MM): ").strip()

    return {
      "cpf_paciente": cpf_paciente,
      "cpf_profissional": cpf_profissional,
      "codigo_tipo_atendimento": codigo_tipo,
      "data_hora": data_hora
    }

  def mostra_atendimento(self, atendimento):
    """Exibe o espelho completo da consulta/atendimento."""
    print(f"ID do Atendimento: {atendimento.id}")
    print(f"Data/Hora: {atendimento.data_hora_str}")
    print(f"Paciente: {atendimento.paciente.nome}")
    print(f"Profissional: {atendimento.profissional.nome} ({atendimento.profissional.registro_profissional})")
    print(f"Tipo: {atendimento.tipo_atendimento.nome}")

    print("Procedimentos Vinculados:")
    if atendimento.procedimentos:
      for proc in atendimento.procedimentos:
        print(f"  - {proc.nome} (R$ {proc.valor:.2f})")
    else:
      print("  - Nenhum procedimento extra cadastrado.")

    print(f"Status do Atendimento: {atendimento.status}")
    print("-" * 50)

  def seleciona_atendimento(self) -> int:
    """Pede o ID único do atendimento para operações."""
    print("\n----- SELECIONAR ATENDIMENTO -----")
    while True:
      try:
        id_atendimento = int(input("Digite o ID do atendimento: ").strip())
        return id_atendimento
      except ValueError:
        print("Por favor, digite um ID numérico inteiro válido.")

  def mostra_mensagem(self, message: str):
    print(f"\n[Atendimento]: {message}")