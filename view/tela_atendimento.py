from exceptions.dado_invalido_exception import DadoInvalidoException
from datetime import date, time


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

    def __valida_data(self, texto: str) -> str:
        try:
            partes = texto.split('/')
            if len(partes) != 3:
                raise ValueError
            dia, mes, ano = map(int, partes)
            date(ano, mes, dia)
            return texto
        except ValueError:
            raise DadoInvalidoException("Data inválida. Use o formato DD/MM/AAAA com valores reais.")

    def __valida_hora(self, texto: str) -> str:
        try:
            partes = texto.split(':')
            if len(partes) != 2:
                raise ValueError
            h, m = map(int, partes)
            time(h, m)
            return texto
        except ValueError:
            raise DadoInvalidoException("Horário inválido. Use o formato HH:MM com valores reais (ex: 08:30).")

    def __pede_texto_obrigatorio(self, prompt: str) -> str:
        while True:
            valor = input(prompt).strip()
            if valor:
                return valor
            print("[Erro]: Este campo não pode ficar em branco.")

    def pega_dados_atendimento(self):
        print("\n----- INSERIR DADOS DO AGENDAMENTO -----")

        cnpj_clinica     = self.__pede_texto_obrigatorio("CNPJ da Clínica (apenas números): ")
        cpf_paciente     = self.__pede_texto_obrigatorio("CPF do Paciente: ")
        cpf_profissional = self.__pede_texto_obrigatorio("CPF do Profissional: ")
        descricao_tipo   = self.__pede_texto_obrigatorio("Descrição do Tipo de Atendimento (ex: Consulta): ")

        while True:
            data = input("Data (DD/MM/AAAA): ").strip()
            try:
                self.__valida_data(data)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            hora_inicio = input("Hora Início (HH:MM): ").strip()
            try:
                self.__valida_hora(hora_inicio)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            hora_fim = input("Hora Fim (HH:MM): ").strip()
            try:
                self.__valida_hora(hora_fim)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            try:
                valor = float(input("Valor Base (R$): ").strip())
                if valor <= 0:
                    print("[Erro]: O valor deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("[Erro]: Valor deve ser numérico.")

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

    def pega_dados_alteracao(self):
        print("\n----- ALTERAR AGENDAMENTO -----")

        while True:
            data = input("Nova Data (DD/MM/AAAA): ").strip()
            try:
                self.__valida_data(data)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            hora_inicio = input("Nova Hora Início (HH:MM): ").strip()
            try:
                self.__valida_hora(hora_inicio)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            hora_fim = input("Nova Hora Fim (HH:MM): ").strip()
            try:
                self.__valida_hora(hora_fim)
                break
            except DadoInvalidoException as e:
                print(f"[Erro]: {e}")

        while True:
            try:
                valor = float(input("Novo Valor Base (R$): ").strip())
                if valor <= 0:
                    print("[Erro]: O valor deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("[Erro]: O valor deve ser numérico.")

        return {
            "data":        data,
            "hora_inicio": hora_inicio,
            "hora_fim":    hora_fim,
            "valor":       valor
        }

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

    def mostra_lista_atendimento(self, indice: int, atendimento):
        print(f"\n[{indice}]")
        self.mostra_atendimento(atendimento)

    def seleciona_atendimento(self) -> int:
        print("\n----- SELECIONAR ATENDIMENTO -----")
        while True:
            try:
                return int(input("Digite o índice [número entre colchetes]: ").strip())
            except ValueError:
                print("[Erro]: Por favor, digite um número inteiro válido.")

    def pega_id_procedimento(self) -> int:
        while True:
            try:
                return int(input("Digite o ID do procedimento: ").strip())
            except ValueError:
                print("[Erro]: ID deve ser um número inteiro.")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Atendimento]: {mensagem}")