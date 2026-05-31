class TelaPagamento():
  # classe pagamento é abstrata. As classes de pagamento específico (cartão, pix) herdam dela.
  def tela_opcoes(self):
    print("-------- PAGAMENTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Pagamento")
    print("2 - Alterar Pagamento")
    print("3 - Listar Pagamentos")
    print("4 - Excluir Pagamento")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass