from exceptions.dado_invalido_exception import DadoInvalidoException
from datetime import date


class TelaPagamento:
    def tela_opcoes(self):
        """Mostra o menu com as opções disponíveis: Incluir, Alterar, Listar e Excluir."""
        print("-------- MENU PAGAMENTOS ----------")
        print("1 - Incluir: registrar pagamento")
        print("2 - Alterar: corrigir/atualizar data de pagamento")
        print("3 - Listar: exibir histórico de pagamentos")
        print("4 - Excluir: estornar/cancelar pagamento")
        print("0 - Retornar ao Menu Principal")
        print("-----------------------------------")

        while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                raise DadoInvalidoException("Opção inválida! Escolha um número entre 0 e 4.")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")


    def mostra_atendimentos_pendentes(self, atendimentos: list):
        print("\n----- ATENDIMENTOS DISPONÍVEIS -----")
        for i, at in enumerate(atendimentos):
            total = at.valor + at.calcular_total_procedimentos()
            print(f"[{i}] {at.paciente.nome} - R$ {total:.2f} - {at.data.strftime('%d/%m/%Y')}")
        print("-------------------------------------")


    def seleciona_atendimento(self) -> int:
        while True:
            try:
                entrada = input("Digite o índice (número entre colchetes) do atendimento: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                return int(entrada)
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")


    def __valida_data(self, texto: str) -> str:
        try:
            partes = texto.split('/')
            if len(partes) != 3:
                raise ValueError
            dia, mes, ano = map(int, partes)
            date(ano, mes, dia)  # lança ValueError se data impossível (ex: 30/02/2024)
            return texto
        except ValueError:
            raise DadoInvalidoException("Data inválida. Use o formato DD/MM/AAAA com valores reais.")


    def pega_dados_pagamento(self, valor_total_atendimento: float):
        print(f"\n----- REGISTRAR PAGAMENTO -----")
        print(f"Valor total do atendimento: R$ {valor_total_atendimento:.2f}")

        while True:
            data_pgto = input("Data do pagamento (DD/MM/AAAA): ").strip()
            try:
                self.__valida_data(data_pgto)
                break
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

        while True:
            try:
                entrada_valor = input(f"Valor a ser pago agora (Max R$ {valor_total_atendimento:.2f}): ").strip()
                if not entrada_valor.replace('.', '', 1).isdigit():
                    raise DadoInvalidoException("Digite um valor numérico válido (exemplo: 150.50).")
                valor_pago = float(entrada_valor)
                if 0 < valor_pago <= valor_total_atendimento:
                    break
                raise DadoInvalidoException(f"O valor pago deve ser maior que 0 e menor ou igual a {valor_total_atendimento:.2f}")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

        print("\nFormas de Pagamento disponíveis no sistema:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão (Crédito ou Débito)")

        while True:
            forma = input("Escolha a forma de pagamento (1, 2 ou 3): ").strip()
            if forma in ["1", "2", "3"]:
                return {
                    "data_pgto": data_pgto,
                    "valor_pago": valor_pago,
                    "forma_pagamento": forma
                }
            print("\n[Erro]: Opção inválida! Escolha 1, 2 ou 3.\n")


    def pega_dados_dinheiro(self, valor_pago: float) -> dict:
        while True:
            try:
                entrada = input(f"Quantia entregue em dinheiro (Mínimo R$ {valor_pago:.2f}): ").strip()
                if not entrada.replace('.', '', 1).isdigit():
                    raise DadoInvalidoException("Digite um valor numérico válido.")
                quantia = float(entrada)
                if quantia >= valor_pago:
                    return {"quantia_entregue": quantia}
                raise DadoInvalidoException("A quantia entregue não pode ser menor que o valor a ser pago.")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")


    def pega_dados_pix(self) -> dict:
        while True:
            cpf = input("Digite apenas os dígitos do CPF, 11 dígitos:  ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                return {"cpf_pagador": cpf}
            print("\n[Erro]: O CPF deve conter exatamente 11 números, sem letras ou símbolos.\n")


    def pega_dados_cartao(self) -> dict:
        while True:
            numero = input("Número do cartão (13 a 19 números): ").strip()
            if numero.isdigit() and 13 <= len(numero) <= 19:
                break
            print("\n[Erro]: O número deve conter entre 13 e 19 dígitos numéricos.\n")

        while True:
            bandeira = input("Bandeira do cartão (Exemplo: Visa, Mastercard): ").strip()
            if bandeira:
                break
            print("\n[Erro]: A bandeira não pode ficar em branco.\n")

        while True:
            tipo = input("Tipo do cartão (digite Credito ou Debito): ").strip().upper()
            if tipo in ["CRÉDITO", "DÉBITO", "CREDITO", "DEBITO"]:
                tipo = "CRÉDITO" if tipo in ["CRÉDITO", "CREDITO"] else "DÉBITO"
                break
            print("\n[Erro]: Escolha entre 'Credito' ou 'Debito'.\n")

        return {
            "numero_cartao": numero,
            "bandeira": bandeira,
            "tipo_cartao": tipo
        }


    def pega_nova_data(self) -> str:
        while True:
            nova_data = input("Digite a nova data do pagamento (DD/MM/AAAA): ").strip()
            try:
                self.__valida_data(nova_data)
                return nova_data
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")


    def seleciona_pagamento(self) -> int:
        while True:
            try:
                entrada = input("Digite o índice (número entre colchetes) do pagamento desejado: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                return int(entrada)
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")


    def mostra_comprovante(self, texto: str):
        print(f"\n{texto}")


    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Sistema Financeiro]: {mensagem}\n")