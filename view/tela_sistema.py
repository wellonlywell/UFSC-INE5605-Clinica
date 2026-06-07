from exceptions.dado_invalido_exception import DadoInvalidoException


class TelaSistema:
    def tela_opcoes(self):
        print("\n========== SisClínica ==========")
        print("1 - Gerenciar Clínicas")
        print("2 - Gerenciar Profissionais")
        print("3 - Gerenciar Tipos de Atendimento")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Pacientes")
        print("6 - Gerenciar Responsáveis")
        print("7 - Gerenciar Atendimentos")
        print("8 - Gerenciar Pagamentos")
        print("9 - Emitir Relatórios")
        print("0 - Sair")
        print("================================")
        while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return opcao
                raise DadoInvalidoException("Opção inválida! Digite um número correspondente ao menu.")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Sistema]: {mensagem}")
