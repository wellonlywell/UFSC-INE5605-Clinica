# classe pagamento é abstrata. As classes de pagamento específico (cartão, pix, dinheiro) herdam dela.

from exceptions.dado_invalido_exception import DadoInvalidoException


class TelaPagamento:
  def tela_opcoes(self):
    """Mostra o menu com as opções disponíveis: Incluir, Listar, Alterar e Excluir."""
    print("-------- MENU PAGAMENTOS ----------")
    print("1 - Incluir: Registrar Pagamento")
    print("2 - Alterar: Corrigir/Alterar Data de Pagamento")
    print("3 - Listar: Listar Histórico de Pagamentos")
    print("4 - Excluir: Estornar/Cancelar Pagamento")
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

  def seleciona_atendimento(self) -> int:
        """Solicita ao usuário o índice do atendimento que receberá o pagamento."""
        while True:
            try:
                entrada = input("Digite o índice (número entre colchetes) do atendimento que deseja pagar: ").strip()
                if not entrada.isdigit():
                  raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                return int(entrada)
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

  def pega_dados_pagamento(self, valor_total_atendimento: float):
        """Coleta os dados iniciais necessários para qualquer forma de pagamento."""
        print(f"\n----- REGISTRAR PAGAMENTO -----")
        print(f"Valor total do atendimento: R$ {valor_total_atendimento:.2f}")
        
        while True:
            data_pgto = input("Data do pagamento (DD/MM/AAAA): ").strip()
            if len(data_pgto) == 10:
                break
            print("\n[Erro]: Formato inválido. Use o padrão DD/MM/AAAA.\n")

        while True:
            try:
                entrada_valor = input(f"Valor a ser pago agora (Max R$ {valor_total_atendimento:.2f}): ").strip()
                # Substitui ponto por vazio para verificar se é um número válido (ex: 150.50)
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
        """Coleta os dados específicos para pagamentos em dinheiro."""
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
        """Coleta os dados específicos para pagamentos via PIX."""
        while True:
            cpf = input("CPF do pagador (Apenas os 11 números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                return {"cpf_pagador": cpf}
            print("\n[Erro]: O CPF deve conter exatamente 11 números, sem letras ou símbolos.\n")

  def pega_dados_cartao(self) -> dict:
        """Coleta os dados específicos para pagamentos em cartão."""
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
            tipo = input("Tipo do cartão (Crédito ou Débito): ").strip().upper()
            if tipo in ["CRÉDITO", "DÉBITO"]:
                break
            print("\n[Erro]: Escolha estritamente entre 'Crédito' ou 'Débito'.\n")

        return {
            "numero_cartao": numero,
            "bandeira": bandeira,
            "tipo_cartao": tipo
        }

  def pega_nova_data(self) -> str:
        """Solicita uma nova data para a função de alteração."""
        while True:
            nova_data = input("Digite a nova data do pagamento (DD/MM/AAAA): ").strip()
            if len(nova_data) == 10:
                return nova_data
            print("\n[Erro]: Formato inválido. Use o padrão DD/MM/AAAA.\n")

  def seleciona_pagamento(self) -> int:
        """Solicita o índice de um pagamento salvo na lista."""
        while True:
            try:
                entrada = input("Digite o índice (número entre colchetes) do pagamento desejado: ").strip()
                if not entrada.isdigit():
                  raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                return int(entrada)
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

  def mostra_mensagem(self, mensagem: str):
        """Exibe mensagens do sistema para usuário."""
        print(f"\n[Sistema Financeiro]: {mensagem}\n")
