
class TelaResponsavel:
  def tela_opcoes(self):
    print("\n-------- MENU RESPONSÁVEIS ----------")
    print("1 - Incluir: cadastrar novo responsável")
    print("2 - Alterar: editar responsável já cadastrado")
    print("3 - Listar: exibir lista de todas pessoas responsáveis cadastradas")
    print("4 - Excluir: remover um responsável do sistema")
    print("0 - Retornar")
    print("-------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_responsavel(self):
    print("\n----- INSERIR DADOS DO RESPONSÁVEL -----")
    cpf = input("CPF (apenas números): ").strip()
    nome_civil = input("Nome Civil: ").strip()
    nome_social = input("Nome Social (Deixe vazio se não houver): ").strip()
    celular = input("Celular (Ex: 48999998888): ").strip()
    parentesco = input("Grau de Parentesco/Vínculo (Ex: Mãe, Pai, Tutor): ").strip()

    while True:
      pcd_input = input("É Pessoa com Deficiência (PCD)? (S/N): ").strip().upper()
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
      "parentesco": parentesco,
      "pcd": pcd,
      "cor_raca_opcao": cor_opcao,
      "identidade_genero": identidade_genero if identidade_genero else "Prefiro não responder"
    }

  def mostra_responsavel(self, responsavel):
    print(f"CPF: {responsavel.cpf}")
    print(f"Nome: {responsavel.nome}")
    print(f"Celular: {responsavel.celular}")
    print(f"Parentesco/Vínculo: {responsavel.parentesco}")
    print(f"PCD: {'Sim' if responsavel.pcd else 'Não'}")

    if responsavel.cor_raca:
      print(f"Cor/Raça: {responsavel.cor_raca.value}")
    if responsavel.identidade_genero:
      print(f"Gênero: {responsavel.identidade_genero}")
    print("-" * 40)

  def seleciona_responsavel(self) -> str:
    print("\n----- SELECIONAR RESPONSÁVEL -----")
    cpf = input("Digite o CPF da pessoa responsável: ").strip()
    return cpf

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")