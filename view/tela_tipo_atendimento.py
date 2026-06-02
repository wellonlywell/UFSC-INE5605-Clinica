
class TelaTipoAtendimento:
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    """Mostra o menu de opções para Tipos de Atendimento."""
    print("-------- TIPOS DE ATENDIMENTO ----------")
    print("1 - Incluir Tipo de Atendimento")
    print("2 - Alterar Tipo de Atendimento")
    print("3 - Listar Tipos de Atendimento")
    print("4 - Excluir Tipo de Atendimento")
    print("0 - Retornar")
    print("----------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_tipo_atendimento(self):
    """Pede os dados para cadastrar ou alterar um tipo de atendimento."""
    print("\n----- INSERIR DADOS DO TIPO DE ATENDIMENTO -----")
    codigo = input("Código identificador (Ex: 101, RE, AMB): ").strip().upper()
    nome = input("Nome do Tipo de Atendimento (Ex: Consulta Eletiva, Retorno): ").strip()

    return {
      "codigo": codigo,
      "nome": nome
    }

  def mostra_tipo_atendimento(self, tipo_atendimento):
    """Exibe os dados de um tipo de atendimento cadastrado."""
    print(f"Código: {tipo_atendimento.codigo}")
    print(f"Nome: {tipo_atendimento.nome}")
    print("-" * 40)

  def seleciona_tipo_atendimento(self) -> str:
    """Pede o código para encontrar um tipo de atendimento específico."""
    print("\n----- SELECIONAR TIPO DE ATENDIMENTO -----")
    codigo = input("Digite o CÓDIGO do tipo de atendimento: ").strip().upper()
    return codigo

  def mostra_mensagem(self, mensagem: str):
    """Mostra qualquer mensagem de sucesso ou erro no terminal."""
    print(f"\n[Aviso]: {mensagem}")