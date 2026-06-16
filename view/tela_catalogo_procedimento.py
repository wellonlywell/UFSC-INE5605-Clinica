from exceptions.dado_invalido_exception import DadoInvalidoException


class TelaCatalogoProcedimento:

    def tela_opcoes(self):
        """Mostra o menu com as opções disponíveis."""
        print("-------- MENU: CATÁLOGO DE PROCEDIMENTOS ----------")
        print("1 - Incluir: cadastrar novo procedimento (ex: Hemograma, Raio-X, etc)")
        print("2 - Alterar: editar procedimento já cadastrado")
        print("3 - Listar: exibir lista de procedimentos cadastrados")
        print("4 - Excluir: remover um procedimento do sistema")
        print("0 - Retornar ao Menu Principal")
        print("---------------------------------------------------")
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

    def pega_dados_procedimento(self):
        print("\n----- INSERIR DADOS DO PROCEDIMENTO -----")

        while True:
            descricao = input("Descrição do Procedimento (Ex: Hemograma, Curativo): ").strip()
            if descricao:
                break
            print("[Erro]: A descrição não pode ficar em branco.")

        while True:
            try:
                custo = float(input("Custo do Procedimento em R$ (Ex: 150.50): ").strip())
                if custo <= 0:
                    print("[Erro]: O custo deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("[Erro]: Digite um valor numérico válido.")

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
                return int(input("Digite o ID do procedimento (ou 0 para cancelar): ").strip())
            except ValueError:
                print("[Erro]: Digite um número inteiro válido.")
  
    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Aviso]: {mensagem}")