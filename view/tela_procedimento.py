from exceptions.dado_invalido_exception import DadoInvalidoException

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
        raise DadoInvalidoException("Opção inválida! Digite um número entre 0 e 4.")
      except ValueError:
        raise DadoInvalidoException("Digite um número inteiro válido.")
      except DadoInvalidoException as e:
        print(e)

  def pega_dados_procedimento(self):
    print("\n----- INSERIR DADOS DO PROCEDIMENTO -----")
    descricao = input("Descrição do Procedimento (Ex: Hemograma, Curativo): ").strip()
    while True:
      try:
        custo = float(input("Custo do Procedimento em R$ (Ex: 150.50): ").strip())
        if custo >= 0:
          break
        raise DadoInvalidoException("O custo não pode ser negativo.")
      except ValueError:
        raise DadoInvalidoException("Digite um valor numérico válido.")
      except DadoInvalidoException as e:
        print(e)
    return {"descricao": descricao, "custo": custo}

  def mostra_procedimento(self, procedimento):
    print(f"ID: {procedimento.id}")
    print(f"Descrição: {procedimento.descricao}")
    print(f"Custo: R$ {procedimento.custo:.2f}")
    print("-" * 40)

  def seleciona_procedimento(self) -> int:
    print("\n----- SELECIONAR PROCEDIMENTO -----")
    while True:
      try:
        id = int(input("Digite o ID do procedimento: ").strip())
        return id
      except ValueError:
        raise DadoInvalidoException("Digite um número inteiro válido.")
      except DadoInvalidoException as e:
        print(e)

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")
