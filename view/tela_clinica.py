
class TelaClinica:
    def tela_opcoes(self):
        print("-------- GERENCIAR CLÍNICAS ----------")
        print("1 - Incluir: Registrar Clínica")
        print("2 - Alterar: Dados de uma Clínica")
        print("3 - Listar: Clínicas")
        print("4 - Excluir: Clínica")
        print("5 - Vincular Profissional à Clínica")
        print("6 - Remover Profissional da Clínica")
        print("7 - Listar Profissionais da Clínica")
        print("0 - Retornar ao Menu Principal")
        print("--------------------------------------")

       while True:
         try:
           opcao = int(input("Escolha a opção: "))
           if opcao in [0, 1, 2, 3, 4, 5, 6, 7]:
             return opcao
           print("Opção inválida! Digite um número entre 0 e 7.")
         except ValueError:
             print("Por favor, digite um número inteiro válido.")

    def pega_dados_clinica(self):
        print("\n----- INSERIR DADOS DA CLÍNICA -----")
        nome = input("Nome Fantasia: ").strip()
        cnpj = input("CNPJ (Digite apenas os dígitos do CNPJ, 14 dígitos ): ").strip()
        cidade = input("Cidade: ").strip()
        descricao = input("Descrição: ").strip()
        horario_abertura = input("Horário de Abertura (HH:MM): ").strip()
        horario_fechamento = input("Horário de Fechamento (HH:MM): ").strip()

        return {
         "nome": nome,
         "cnpj": cnpj,
         "cidade": cidade,
         "descricao": descricao,
         "horario_abertura": horario_abertura,
         "horario_fechamento": horario_fechamento   }

    def mostra_clinica(self, clinica):
        print(f"CNPJ: {clinica.cnpj}")
        print(f"Nome: {clinica.nome}")
        print(f"Cidade: {clinica.cidade}")
        print(f"Descrição: {clinica.descricao}")
        print(f"Horário de Abertura: {clinica.horario_abertura.strftime('%H:%M')}")
        print(f"Horário de Fechamento: {clinica.horario_fechamento.strftime('%H:%M')}")
        print("-" * 40)

    def seleciona_clinica(self) -> str:
        print("\n----- SELECIONAR CLÍNICA -----")
        cnpj = input("Digite o CNPJ da clínica: ").strip()
        return cnpj

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Clínica]: {mensagem}")

    def seleciona_profissional(self) -> str:
        print("\n----- SELECIONAR PROFISSIONAL -----")
        cpf = input("Digite o CPF do profissional: ").strip()
        return cpf

    def mostra_profissionais_da_clinica(self, clinica):
        print(f"\nProfissionais vinculados à clínica {clinica.nome}:")
        profissionais = clinica.profissionais
        if not profissionais:
            print("Nenhum profissional vinculado a esta clínica.")
        return

for profissional in profissionais:
    print(f"CPF: {profissional.cpf}")
    print(f"Nome: {profissional.nome_exibicao}")
    print(f"Especialidade: {profissional.especialidade}")
    print("-" * 40)
