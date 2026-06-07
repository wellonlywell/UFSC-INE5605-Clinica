
class TelaRelatorios:
  def tela_opcoes(self):
    """Exibe o menu de emissão de relatórios estatísticos e indicadores de gestão e equidade em saúde."""
    print("-------- RELATÓRIOS E INDICADORES ----------")
    print("1 - Clínicas com maior número de atendimentos")
    print("2 - Atendimentos mais caros e mais baratos")
    print("3 - Procedimentos mais realizados (populares)")
    print("4 - Procedimentos mais caros e mais baratos")
    print("5 - Indicadores de Equidade (PCD, Cor/Raça, Gênero)")
    print("0 - Retornar ao Menu Principal")
    print("--------------------------------------------")

    while True:
      try:
        opcao = int(input("Escolha a opção: "))
        if opcao in [0, 1, 2, 3, 4, 5]:
          return opcao
        print("Opção inválida! Digite um número entre 0 e 5.")
      except ValueError:
        print("Por favor, digite um número inteiro válido.")

  def exibe_dados_relatorio(self, dados_formatados: str):
    print("\n================ RELATÓRIO EMITIDO ================")
    print(dados_formatados)
    print("===================================================")
    input("\nPressione ENTER para retornar ao menu...")

  def mostra_mensagem(self, mensagem: str):
    print(f"\n[Relatório]: {mensagem}")