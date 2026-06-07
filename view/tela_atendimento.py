class TelaAtendimento:

    def tela_opcoes(self):
        print("\n-------- MENU AGENDAMENTOS/ATENDIMENTOS ----------")
        print("1 - Agendar Novo Atendimento")
        print("2 - Alterar Atendimento")
        print("3 - Listar Todos os Atendimentos")
        print("4 - Cancelar Atendimento")
        print("0 - Retornar ao Menu Principal")
        print("--------------------------------------------------")
        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                print("Opção inválida! Digite um número entre 0 e 4.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    def pega_dados_atendimento(self):
  
        print("\n----- INSERIR DADOS DO AGENDAMENTO -----")
        cnpj_clinica = input("CNPJ da Clínica (apenas números): ").strip()
        cpf_paciente = input("CPF do Paciente (apenas números): ").strip()
        cpf_profissional = input("CPF do Profissional (apenas números): ").strip()
        descricao_tipo = input("Descrição do Tipo de Atendimento (ex: Consulta): ").strip()
        data = input("Data do Atendimento (DD/MM/AAAA): ").strip()
        hora_inicio = input("Hora de Início (HH:MM): ").strip()
        hora_fim = input("Hora de Fim (HH:MM): ").strip()
        while True:
            try:
                valor = float(input("Valor do Atendimento (R$): ").strip())
                if valor > 0:
                    break
                print("O valor deve ser maior que zero.")
            except ValueError:
                print("Digite um número válido.")
        return {
            "cnpj_clinica": cnpj_clinica,
            "cpf_paciente": cpf_paciente,
            "cpf_profissional": cpf_profissional,
            "descricao_tipo": descricao_tipo,
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "valor": valor
        }

    def mostra_atendimento(self, atendimento):
        """
        CORRIGIDO: A versão original acessava:
          atendimento.id          → não existe
          atendimento.data_hora_str → não existe
          atendimento.profissional.registro_profissional → o atributo correto é .registro
          atendimento.tipo_atendimento.nome → o atributo correto é .tipo.descricao
          atendimento.status      → não existe
          proc.nome, proc.valor   → os atributos corretos são .descricao e .custo
        Agora usa apenas atributos que realmente existem no model.
        """
        print(f"Paciente: {atendimento.paciente.nome}")
        print(f"Profissional: {atendimento.profissional.nome} ({atendimento.profissional.registro})")
        print(f"Clínica: {atendimento.clinica.nome}")
        print(f"Tipo: {atendimento.tipo.descricao}")
        print(f"Data: {atendimento.data.strftime('%d/%m/%Y')}  "
              f"{atendimento.hora_inicio.strftime('%H:%M')} - {atendimento.hora_fim.strftime('%H:%M')}")
        print(f"Valor: R$ {atendimento.valor:.2f}")
        print("Procedimentos:")
        if atendimento.procedimentos:
            for proc in atendimento.procedimentos:
                print(f"  - {proc.descricao} (R$ {proc.custo:.2f})")
        else:
            print("  - Nenhum procedimento cadastrado.")
        print("-" * 50)

    def seleciona_atendimento(self) -> int:
        print("\n----- SELECIONAR ATENDIMENTO -----")
        while True:
            try:
                return int(input("Digite o número do atendimento (entre colchetes): ").strip())
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Atendimento]: {mensagem}")
