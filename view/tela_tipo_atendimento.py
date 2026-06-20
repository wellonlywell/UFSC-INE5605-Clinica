from exceptions.dado_invalido_exception import DadoInvalidoException

class TelaTipoAtendimento:
  def tela_opcoes(self):
    """Mostra o menu com as opções disponíveis: Incluir, Listar, Alterar e Excluir."""
    print("-------- TIPOS DE ATENDIMENTO ----------")
    print("1 - Incluir: cadastrar novo tipo (ex: Consulta, Exame, Retorno)")
    print("2 - Alterar: editar um tipo já cadastrado")
    print("3 - Listar: exibir lista de tipos cadastrados")
    print("4 - Excluir: remover um tipo do sistema")
    print("0 - Retornar ao Menu Principal")
    print("----------------------------------------")

    while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                if not entrada.isdigit():
                  raise DadoInvalidoException("Por favor, digite apenas números inteiros.")                
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                  return opcao                
                raise DadoInvalidoException("Opção inválida! Digite um número entre 0 e 4.")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

  def pega_dados_tipo_atendimento(self, operacao="INSERIR"):
        print(f"\n----- {operacao} DADOS DO TIPO DE ATENDIMENTO -----")        
        if operacao == "ALTERAR":
            print("Digite a nova descrição para substituir a atual:")
        else:
            print("Digite a descrição do novo tipo de atendimento:")

        while True:
            descricao = input("Descrição (Ex: Consulta Eletiva, Retorno): ").strip()
            if descricao:
              return {"descricao": descricao}
            print("\n[Erro]: A descrição não pode ficar em branco.\n")

  def mostra_tipo_atendimento(self, tipo_atendimento):
        print(f"ID: {tipo_atendimento.id}")
        print(f"Descrição: {tipo_atendimento.descricao}")
        print("-" * 40)

  def seleciona_tipo_atendimento(self) -> int:
        print("\n----- SELECIONAR TIPO DE ATENDIMENTO -----")
        while True:
            try:
                entrada = input("Digite o ID do tipo de atendimento (ou 0 para cancelar): ").strip()
                if not entrada.isdigit():
                  raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                return int(entrada)
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Aviso]: {mensagem}")