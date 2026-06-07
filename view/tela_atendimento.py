from exceptions.dado_invalido_exception import DadoInvalidoException


class TelaAtendimento:

    def tela_opcoes(self):
        """Mostra o menu com as opções disponíveis."""
        print("\n-------- MENU AGENDAMENTOS/ATENDIMENTOS ----------")
        print("1 - Incluir: agendar novo atendimento")
        print("2 - Alterar: atualizar data/hora/valor")
        print("3 - Listar: exibir todos os atendimentos")
        print("4 - Excluir: cancelar atendimento")
        print("5 - Registrar procedimentos realizados")
        print("0 - Retornar ao Menu Principal")
        print("--------------------------------------------------")
        while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Digite apenas números.")
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                print("Opção inválida! Escolha um número entre 0 e 5.")
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

    def pega_dados_atendimento(self):
      
        print("\n----- INSERIR DADOS DO AGENDAMENTO -----")
        try:
            cnpj_clinica    = input("CNPJ da Clínica (apenas números): ").strip()
            cpf_paciente    = input("CPF do Paciente: ").strip()
            cpf_profissional = input("CPF do Profissional: ").strip()
            descricao_tipo  = input("Descrição do Tipo de Atendimento (ex: Consulta): ").strip()
            data            = input("Data (DD/MM/AAAA): ").strip()
            hora_inicio     = input("Hora Início (HH:MM): ").strip()
            hora_fim        = input("Hora Fim (HH:MM): ").strip()
            valor           = float(input("Valor Base (R$): ").strip())
            return {
                "cnpj_clinica":     cnpj_clinica,
                "cpf_paciente":     cpf_paciente,
                "cpf_profissional": cpf_profissional,
                "descricao_tipo":   descricao_tipo,
                "data":             data,
                "hora_inicio":      hora_inicio,
                "hora_fim":         hora_fim,
                "valor":            valor
            }
        except ValueError:
            raise DadoInvalidoException("Valor deve ser numérico.")

    def pega_dados_alteracao(self):
  
        print("\n----- ALTERAR AGENDAMENTO -----")
        try:
            return {
                "data":        input("Nova Data (DD/MM/AAAA): ").strip(),
                "hora_inicio": input("Nova Hora Início (HH:MM): ").strip(),
                "hora_fim":    input("Nova Hora Fim (HH:MM): ").strip(),
                "valor":       float(input("Novo Valor Base (R$): ").strip())
            }
        except ValueError:
            raise DadoInvalidoException("O valor deve ser numérico.")

    def mostra_atendimento(self, atendimento):
      
        print(f"Data/Hora: {atendimento.data.strftime('%d/%m/%Y')} "
              f"das {atendimento.hora_inicio.strftime('%H:%M')} "
              f"às {atendimento.hora_fim.strftime('%H:%M')}")
        print(f"Clínica:      {atendimento.clinica.nome}")
        print(f"Paciente:     {atendimento.paciente.nome}")
        print(f"Profissional: {atendimento.profissional.nome} "
              f"(Registro: {atendimento.profissional.registro})")
        print(f"Tipo:         {atendimento.tipo.descricao}")
        print(f"Valor base:   R$ {atendimento.valor:.2f}")

        print("Procedimentos realizados:")
        if atendimento.procedimentos:
            for proc in atendimento.procedimentos:
                print(f"  - {proc.descricao} (R$ {proc.custo:.2f})")
        else:
            print("  - Nenhum procedimento cadastrado.")

        total = atendimento.valor + atendimento.calcular_total_procedimentos()
        print(f"VALOR TOTAL: R$ {total:.2f}")
        print("-" * 50)

    def seleciona_atendimento(self) -> int:
        """Pede o índice (número entre colchetes) do atendimento para operações."""
        print("\n----- SELECIONAR ATENDIMENTO -----")
        while True:
            try:
                return int(input("Digite o índice [número entre colchetes]: ").strip())
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    def pega_id_procedimento(self) -> int:
        """Pede o ID do procedimento do catálogo para adicionar ao atendimento."""
        try:
            return int(input("Digite o ID do procedimento: ").strip())
        except ValueError:
            raise DadoInvalidoException("ID deve ser um número inteiro.")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Atendimento]: {mensagem}")
