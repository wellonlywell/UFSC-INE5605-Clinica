# class feita por Well

class TelaProcedimento:
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    """Mostra o menu de opções para Procedimentos."""
    print("-------- MENU PROCEDIMENTOS ----------")
    print("1 - Incluir Procedimento")
    print("2 - Alterar Procedimento")
    print("3 - Listar Procedimentos")
    print("4 - Excluir Procedimento")
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

  def pega_dados_procedimento(self):
    """Pede os dados para cadastrar ou alterar um procedimento clínico."""
    print("\n----- INSERIR DADOS DO PROCEDIMENTO -----")
    codigo = input("Código do Procedimento (Ex: HEMO, RAIOX, CURAT): ").strip().upper()
    nome = input("Nome do Procedimento (Ex: Hemograma Completo): ").strip()

    # Validação para garantir que o valor seja um número real (float) válido
    while True:
      try:
        valor = float(input("Valor do Procedimento em R$ (Ex: 150.50): ").strip())
        if valor >= 0:
          break
        print("O valor do procedimento não pode ser negativo.")
      except ValueError:
        print("Por favor, digite um valor numérico válido (use ponto para centavos).")

    return {
      "codigo": codigo,
      "nome": nome,
      "valor": valor
    }

  def mostra_procedimento(self, procedimento):
    """Exibe os dados de um procedimento cadastrado."""
    print(f"Código: {procedimento.codigo}")
    print(f"Nome: {procedimento.nome}")
    print(f"Valor: R$ {procedimento.valor:.2f}")
    print("-" * 40)

  def seleciona_procedimento(self) -> str:
    """Pede o código para encontrar um procedimento específico."""
    print("\n----- SELECIONAR PROCEDIMENTO -----")
    codigo = input("Digite o CÓDIGO do procedimento: ").strip().upper()
    return codigo

  def mostra_mensagem(self, mensagem: str):
    """Mostra qualquer mensagem de sucesso ou erro no terminal."""
    print(f"\n[Aviso]: {mensagem}")
