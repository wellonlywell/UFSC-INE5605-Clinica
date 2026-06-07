# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
from exceptions.dado_invalido_exception import DadoInvalidoException

class TelaAtendimento:
  def tela_opcoes(self):
    """Mostra o menu com as opções disponíveis: Incluir, Listar, Alterar e Excluir."""
    print("\n-------- MENU AGENDAMENTOS/ATENDIMENTOS ----------")
    print("1 - Incluir: agendar novo atendimento")
    print("2 - Alterar: atualizar data/hora/valor de agendamento")
    print("3 - Listar: exibir lista de todos os atendimentos")
    print("4 - Excluir: cancelar atendimento já cadastrados")
    print("5 - Registrar procedimentos realizados (Itens da consulta)")
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
        else:
          print("Opção inválida! Escolha um número entre 0 e 5.")
      except DadoInvalidoException as e:
        print(f"[Erro]: {e}")

  # Métodos para cada operação (Incluir, Listar, Alterar, Excluir) podem ser implementados aqui.
  def pega_dados_atendimento(self):
    try:
      dados = {
        "cnpj_clinica": input("CNPJ da Clínica (apenas números): ").strip(),
        "cpf_paciente": input("CPF do Paciente: ").strip(),
        "cpf_profissional": input("CPF do Profissional: ").strip(),
        "id_tipo": int(input("ID do Tipo de Atendimento: ").strip()),
        "data": input("Data (DD/MM/AAAA): ").strip(),
        "hora_inicio": input("Hora Início (HH:MM): ").strip(),
        "hora_fim": input("Hora Fim (HH:MM): ").strip(),
        "valor": float(input("Valor Base (R$): ").strip())
        }
      return dados
    except ValueError:
      raise DadoInvalidoException("ID e Valor devem ser numéricos.")

  # Método para pegar dados de alteração, caso o usuário queira atualizar um atendimento já cadastrado
  def pega_dados_alteracao(self):
        """Pede apenas os dados que podem ser alterados em um agendamento existente."""
        print("\n----- ALTERAR AGENDAMENTO -----")
        try:
            return {
                "data": input("Nova Data: ").strip(),
                "hora_inicio": input("Nova Hora Início: ").strip(),
                "hora_fim": input("Nova Hora Fim: ").strip(),
                "valor": float(input("Novo Valor Base: ").strip())
            }
        except ValueError:
            raise DadoInvalidoException("O valor deve ser numérico!")
        
  # Método para exibir os detalhes completos de um atendimento, incluindo procedimentos vinculados e valor total. Tipo resumo comprovante da consulta/atendimento.
  def mostra_atendimento(self, atendimento):
    """Exibe o resumo(comprovante) do atendimento."""
    print(f"Data/Hora: {atendimento.data.strftime('%d/%m/%Y')} das {atendimento.hora_inicio.strftime('%H:%M')} às {atendimento.hora_fim.strftime('%H:%M')}")
    print(f"Paciente: {atendimento.paciente.nome}")
    print(f"Profissional: {atendimento.profissional.nome} (Registro: {atendimento.profissional.registro})")
    print(f"Tipo: {atendimento.tipo.descricao}")

    print("Procedimentos Vinculados:")
    if atendimento.procedimentos:      
        for proc in atendimento.procedimentos:
            print(f"  - {proc.descricao} (R$ {proc.custo:.2f})")
    else:
        print("  - Nenhum procedimento extra cadastrado.")
    print("-" * 50)
    total = atendimento.valor + atendimento.calcular_total_procedimentos()
    print(f"VALOR TOTAL: R$ {total:.2f}")

    

  def seleciona_atendimento(self) -> int:
    """Pede o índice da lista (ex: 0, 1, 2) para operações."""
    print("\n----- SELECIONAR ATENDIMENTO -----")
    while True:
      try:
        id_atendimento = int(input("Digite o índice[número entre colchetes] do atendimento: ").strip())
        return id_atendimento
      except ValueError:
        print("Por favor, digite um ID numérico inteiro válido.")
      
  # Método para selecionar aadicionar um procedimento específico a um atendimento já cadastrado, usando o ID do procedimento.
  def pega_id_procedimento(self):
        """Pede o ID do procedimento do catálogo para buscar seus dados e adicionar ao atendimento."""
        try:
            return int(input("Digite o ID do procedimento: ").strip())
        except ValueError:
            raise DadoInvalidoException("ID deve ser um número inteiro.")

  def mostra_mensagem(self, message: str):
    print(f"\n[Atendimento]: {message}")