# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

class TelaProfissional:
  def tela_opcoes(self):
    """Mostra o menu de opções da pessoa Profissional."""
    print("-------- MENU PROFISSIONAIS ----------")
    print("1 - Incluir Profissional")
    print("2 - Alterar Profissional")
    print("3 - Listar Profissionais")
    print("4 - Excluir Profissional")
    print("0 - Retornar ao Menu Principal")
    print("--------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_profissional(self):
    """Pede os dados para cadastrar ou alterar um profissional de saúde."""
    print("\n----- INSERIR DADOS DO PROFISSIONAL -----")
    cpf = input("CPF (apenas números): ").strip()
    nome_civil = input("Nome Civil: ").strip()
    nome_social = input("Nome Social (Deixe vazio se não houver): ").strip()
    celular = input("Celular (Ex: 48999998888): ").strip()
    # DATA DE NASCIMENTO REMOVIDA DAQUI
    registro = input("Registro Profissional (Ex: CRM/SC 12345, COREN 6789): ").strip()
    especialidade = input("Especialidade Médica/Área (Ex: Clínico Geral, Pediatra): ").strip()

    while True:
      pcd_input = input("É Pessoa com Deficiência (PCD)? (S/N): ").strip().upper()
      if pcd_input in ['S', 'N']:
        pcd = (pcd_input == 'S')
        break
      print("Por favor, responda apenas com S ou N.")

    print("\nCor ou raça (autodeclaração — categorias IBGE):")
    print("( 1 ) Branca    ( 2 ) Preta     ( 3 ) Parda")
    print("( 4 ) Amarela   ( 5 ) Indígena  ( 6 ) Prefiro não responder")

    while True:
      cor_opcao = input("Escolha uma opção (1 a 6): ").strip()
      if cor_opcao in ["1", "2", "3", "4", "5", "6"]:
        break
      print("Opção inválida! Digite um número de 1 a 6.")

    print("\n--- Identidade de Gênero ---")
    identidade_genero = input("Sua resposta (Ou pressione ENTER para 'Prefiro não responder'): ").strip()

    return {
      "cpf": cpf,
      "nome_civil": nome_civil,
      "nome_social": nome_social if nome_social else None,
      "celular": celular,
      "registro": registro,
      "especialidade": especialidade,
      "pcd": pcd,
      "cor_raca_opcao": cor_opcao,
      "identidade_genero": identidade_genero if identidade_genero else "Prefiro não responder"
    }

  def mostra_profissional(self, profissional):
    """Exibe os dados extraídos diretamente do objeto Profissional."""
    # CORRIGIDO: Agora puxa .registro e não tem mais print de data
    print(f"Registro Profissional: {profissional.registro}")
    print(f"Especialidade: {profissional.especialidade}")
    print(f"Nome: {profissional.nome}")
    print(f"CPF: {profissional.cpf}")
    print(f"Celular: {profissional.celular}")
    print(f"PCD: {'Sim' if profissional.pcd else 'Não'}")

    if profissional.cor_raca:
      print(f"Cor/Raça: {profissional.cor_raca.value}")
    if profissional.identidade_genero:
      print(f"Gênero: {profissional.identidade_genero}")
    print("-" * 40)

  def seleciona_profissional(self) -> str:
    """Pede o CPF para encontrar um profissional específico."""
    print("\n----- SELECIONAR PROFISSIONAL -----")
    cpf = input("Digite o CPF do profissional: ").strip()
    return cpf

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")