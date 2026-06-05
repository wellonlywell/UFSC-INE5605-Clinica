from exceptions.dado_invalido_exception import DadoInvalidoException

class TelaTipoAtendimento:
  def tela_opcoes(self):
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
        raise DadoInvalidoException("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        raise DadoInvalidoException("Digite um número inteiro válido.")
      except DadoInvalidoException as e:
        print(e)

  def pega_dados_tipo_atendimento(self):
    print("\n----- INSERIR DADOS DO TIPO DE ATENDIMENTO -----")
    descricao = input("Descrição (Ex: Consulta Eletiva, Retorno): ").strip()
    return {"descricao": descricao}

  def mostra_tipo_atendimento(self, tipo_atendimento):
    print(f"ID: {tipo_atendimento.id}")
    print(f"Descrição: {tipo_atendimento.descricao}")
    print("-" * 40)

  def seleciona_tipo_atendimento(self) -> int:
    print("\n----- SELECIONAR TIPO DE ATENDIMENTO -----")
    while True:
      try:
        id = int(input("Digite o ID do tipo de atendimento: ").strip())
        return id
      except ValueError:
        raise DadoInvalidoException("Digite um número inteiro válido.")
      except DadoInvalidoException as e:
        print(e)

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")