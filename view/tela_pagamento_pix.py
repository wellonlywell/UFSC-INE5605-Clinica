class TelaPagamentoPix ():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PAGAMENTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir PagamentoPix")
    print("2 - Alterar PagamentoPix")
    print("3 - Listar PagamentosPix")
    print("4 - Excluir PagamentoPix")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
pass