
class TelaPaciente:
  def tela_opcoes(self):
    print("\n-------- MENU PACIENTES ----------")
    print("1 - Incluir: cadastrar novo paciente")
    print("2 - Alterar: editar paciente já cadastrado")
    print("3 - Listar: exibir lista de todas pessoas pacientes cadastrados")
    print("4 - Excluir: remover um paciente do sistema")
    print("0 - Retornar ao Menu Principal")
    print("----------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_paciente(self):
    print("\n----- INSERIR DADOS DO PACIENTE -----")
    cpf = input("CPF (apenas números): ").strip()
    nome_civil = input("Nome Civil: ").strip()
    nome_social = input("Nome Social (Deixe vazio se não houver): ").strip()
    celular = input("Celular (Ex: 48999998888): ").strip()
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()

    while True:
      pcd_input = input("\nÉ Pessoa com Deficiência (PCD)? (S/N): ").strip().upper()
      if pcd_input in ['S', 'N']:
        pcd = (pcd_input == 'S')
        break
      print("Por favor, responda apenas com S ou N.")

    print("\nAutodeclaração — categorias IBGE:")
    print("Nota: Dados coletados para fins de indicadores de equidade em saúde.")
    print("Como você se autodeclara?")
    print("( 1 ) Branca    ( 2 ) Preta     ( 3 ) Parda")
    print("( 4 ) Amarela   ( 5 ) Indígena  ( 6 ) Prefiro não responder")

    while True:
      cor_opcao = input("Escolha uma opção (1 a 6): ").strip()
      if cor_opcao in ["1", "2", "3", "4", "5", "6"]:
        break
      print("Opção inválida! Digite um número de 1 a 6.")

    print("\n--- Identidade de Gênero ---")
    print("Como você se identifica em relação ao seu gênero atual?")
    print("Exemplos: Mulher Cis/Trans, Homem Cis/Trans, Pessoa não-binária, Gênero fluido, Agênero, etc")
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

  def mostra_paciente(self, paciente):
    print(f"CPF: {paciente.cpf}")
    print(f"Nome: {paciente.nome}")
    print(f"Celular: {paciente.celular}")

    if hasattr(paciente.data_nascimento, 'strftime'):
      data_str = paciente.data_nascimento.strftime('%d/%m/%Y')
    else:
      data_str = paciente.data_nascimento

    print(f"Idade: {paciente.idade} anos (Nascimento: {data_str})")
    print(f"PCD: {'Sim' if paciente.pcd else 'Não'}")

    if paciente.cor_raca:
      print(f"Cor/Raça: {paciente.cor_raca.value}")
    if paciente.identidade_genero:
      print(f"Gênero: {paciente.identidade_genero}")
    if paciente.responsavel:
      print(f"Responsável Legal: {paciente.responsavel.nome}")
    print("-" * 40)

  def seleciona_paciente(self) -> str:
    print("\n----- SELECIONAR PACIENTE -----")
    cpf = input("Digite apenas os dígitos do CPF do paciente: ").strip()
    return cpf

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")