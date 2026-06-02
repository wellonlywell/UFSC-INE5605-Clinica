# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

class TelaClinica:
  def tela_opcoes(self):
    """Mostra o menu completo para gerenciar Clínicas (Escopo do Professor)."""
    print("-------- GERENCIAR CLÍNICAS ----------")
    print("1 - Incluir Clínica")
    print("2 - Alterar Dados de uma Clínica")
    print("3 - Listar Clínicas")
    print("4 - Excluir Clínica")
    print("0 - Retornar")
    print("--------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_clinica(self):
    """Pede as informações básicas para cadastrar/alterar uma clínica."""
    print("\n----- INSERIR DADOS DA CLÍNICA -----")
    nome = input("Nome Fantasia: ").strip()
    cnpj = input("CNPJ (apenas números): ").strip()
    endereco = input("Endereço Completo: ").strip()

    return {
      "nome": nome,
      "cnpj": cnpj,
      "endereco": endereco
    }

  def mostra_clinica(self, clinica):
    """Exibe as informações de uma clínica cadastrada."""
    print(f"CNPJ: {clinica.cnpj}")
    print(f"Nome: {clinica.nome}")
    print(f"Endereço: {clinica.endereco}")
    print("-" * 40)

  def seleciona_clinica(self) -> str:
    """Pede o CNPJ para identificar uma clínica específica."""
    print("\n----- SELECIONAR CLÍNICA -----")
    cnpj = input("Digite o CNPJ da clínica: ").strip()
    return cnpj

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Clínica]: {mensagem}")

