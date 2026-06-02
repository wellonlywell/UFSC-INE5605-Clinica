class TelaPaciente():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    """Mostra o menu de opções da pessoa Paciente."""
    print("-------- MENU PACIENTES ----------")
    print("1 - Incluir Paciente")
    print("2 - Alterar Paciente")
    print("3 - Listar Pacientes")
    print("4 - Excluir Paciente")
    print("0 - Retornar")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_paciente(self):
    """Pede os dados para cadastrar ou alterar um paciente."""
    print("\n----- INSERIR DADOS DO PACIENTE -----")
    cpf = input("CPF (apenas números): ").strip()
    nome_civil = input("Nome Civil: ").strip()
    nome_social = input("Nome Social (Deixe vazio se não houver): ").strip()
    celular = input("Celular (Ex: 48999998888): ").strip()
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()


    pcd_input = input("É Pessoa com Deficiência (PCD)? (S/N): ").strip().upper()
    pcd = True if pcd_input == 'S' else False

    print("\nCores/Raças disponíveis:")
    print("1 - Branca | 2 - Preta | 3 - Parda | 4 - Amarela | 5 - Indígena | 6 - Não Informado")

    # Identidade de gênero aberta
    print("\nComo você se identifica em relação ao seu gênero?")
    print("Exemplos: Mulher Cis/Trans, Homem Cis/Trans, Pessoa não-binária, Gênero fluido, etc")
    identidade_genero = input("Sua resposta (Ou pressione ENTER para 'Prefiro não responder'): ").strip()

    return {
      "cpf": cpf,
      "nome_civil": nome_civil,
      "nome_social": nome_social if nome_social else None,
      "celular": celular,
      "data_nascimento": data_nascimento,
      "pcd": pcd,
      "cor_raca_opcao": cor_opcao,
      "identidade_genero": identidade_genero if identidade_genero else "Prefiro não responder"
    }

  def mostra_paciente(self, dados_paciente: dict):
    """Exibe os dados de um único paciente na tela."""
    print(f"CPF: {dados_paciente['cpf']}")
    print(f"Nome: {dados_paciente['nome']}")
    print(f"Celular: {dados_paciente['celular']}")
    print(f"Idade: {dados_paciente['idade']} anos (Nascimento: {dados_paciente['data_nascimento']})")
    print(f"PCD: {'Sim' if dados_paciente['pcd'] else 'Não'}")
    print(f"Cor/Raça: {dados_paciente['cor_raca']}")
    print(f"Gênero: {dados_paciente['identidade_genero']}")
    if dados_paciente['nome_responsavel']:
      print(f"Responsável Legal: {dados_paciente['nome_responsavel']}")
    print("-" * 40)

  def seleciona_paciente(self) -> str:
    """Pede o CPF para encontrar uma pessoa paciente específico."""
    print("\n----- SELECIONAR PACIENTE -----")
    cpf = input("Digite o CPF do paciente: ").strip()
    return cpf

  def mostra_mensagem(self, mensagem: str):
    """Mostra qualquer mensagem de sucesso ou erro no terminal."""
    print(f"\n[Aviso]: {mensagem}")