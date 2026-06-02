# classe pagamento é abstrata. As classes de pagamento específico (cartão, pix, dinheiro) herdam dela.

class TelaPagamento:
  def tela_opcoes(self):
    """Mostra o menu financeiro de pagamentos."""
    print("-------- MENU PAGAMENTOS ----------")
    print("1 - Registrar Pagamento")
    print("2 - Estornar/Cancelar Pagamento")
    print("3 - Listar Histórico de Pagamentos")
    print("0 - Retornar")
    print("-----------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 3.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def pega_dados_pagamento(self, valor_total: float):
    """Pede os dados para fechar a conta do atendimento."""
    print("\n----- REGISTRAR PAGAMENTO -----")
    print(f"Valor total a ser pago: R$ {valor_total:.2f}")

    print("\nFormas de Pagamento:")
    print("( 1 ) Dinheiro  ( 2 ) Cartão de Débito  ( 3 ) Cartão de Crédito  ( 4 ) PIX")

    while True:
      forma_input = input("Escolha a forma de pagamento (1 a 4): ").strip()
      if forma_input in ["1", "2", "3", "4"]:
        break
      print("Opção inválida! Escolha de 1 a 4.")

    while True:
      try:
        desconto = float(input("Valor do desconto em R$ (Digite 0 se não houver): ").strip())
        if 0 <= desconto <= valor_total:
          break
        print(f"O desconto deve ser entre R$ 0.00 e R$ {valor_total:.2f}.")
      except ValueError:
        print("Por favor, digite um valor numérico válido para o desconto.")

    return {
      "forma_pagamento": forma_input,
      "desconto": desconto
    }

  def mostra_pagamento(self, pagamento):
    """Exibe os dados de um comprovante de pagamento."""
    print(f"ID Pagamento: {pagamento.id}")
    print(f"Forma: {pagamento.forma_pagamento_extenso}")
    print(f"Valor Original: R$ {pagamento.valor_original:.2f}")
    print(f"Desconto aplicado: R$ {pagamento.desconto:.2f}")
    print(f"Valor Final Pago: R$ {pagamento.valor_final:.2f}")
    print(f"Status: {pagamento.status}")
    print("-" * 40)

  def seleciona_pagamento(self) -> int:
    """Pede o ID para localizar um pagamento específico."""
    print("\n----- SELECIONAR PAGAMENTO -----")
    while True:
      try:
        id_pagamento = int(input("Digite o ID do pagamento: ").strip())
        return id_pagamento
      except ValueError:
        print("Por favor, digite um ID numérico inteiro válido.")

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Financeiro]: {mensagem}")

    def mostra_mensagem(self, mensagem: str):
      print(f"\n[Financeiro]: {mensagem}")