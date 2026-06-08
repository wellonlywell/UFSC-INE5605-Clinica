from exceptions.dado_invalido_exception import DadoInvalidoException


class TelaSistema:
    def tela_opcoes(self):
        print("\n========== SisClínica ==========")
        print("1 - Gerenciar Clínicas")
        print("2 - Gerenciar Profissionais")
        print("3 - Gerenciar Tipos de Atendimento")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Pacientes")
        print("6 - Gerenciar Atendimentos")
        print("7 - Gerenciar Pagamentos")
        print("8 - Emitir Relatórios")
        print("0 - Sair: Encerrar sistema")
        print("================================")
        while True:
            try:
                entrada = input("Escolha a opção: ").strip()
                if not entrada.isdigit():
                    raise DadoInvalidoException("Por favor, digite apenas números inteiros.")
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    return opcao
                raise DadoInvalidoException("Opção inválida! Digite um número entre 0 e 8.")
            except DadoInvalidoException as e:
                print(f"\n[Erro]: {e}\n")

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[Sistema]: {mensagem}")