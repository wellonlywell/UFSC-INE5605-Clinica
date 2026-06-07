from exceptions.dado_invalido_exception import DadoInvalidoException

class TelaSistema:
    def tela_opcoes(self):
        """Mostra o menu principal do SisClínica."""
        print("-------- SisClínica ---------")
        print("1 - Gerenciar Clínicas")
        print("2 - Gerenciar Profissionais")
        print("3 - Gerenciar Tipos de Atendimento")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Pacientes")
        print("6 - Gerenciar Agendamentos: Atendimentos")
        print("7 - Gerenciar Pagamentos")
        print("8 - Emitir Relatórios")
        print("0 - Sair: Encerrar sistema")
        print("-----------------------------")

        while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                # Passo 1: Verifica se o que foi digitado é apenas número. 
                # Se for letra ou vazio, levanta a SUA exceção.
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")                
                
                # Passo 2: Agora é seguro converter para inteiro
                opcao = int(entrada)
                
                # Passo 3: Verifica se a opção está na lista                
                if opcao in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    return opcao
                
                # Se digitou um número como 9 ou 99, levanta a SUA exceção.
                raise DadoInvalidoException("Opção inválida! Digite um número correspondente ao menu.")
            except DadoInvalidoException as e:
                # Captura todas as validações acima e mostra a mensagem de erro sem quebrar o sistema
                print(f"\n[Erro]: {e}\n")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Sistema]: {mensagem}")