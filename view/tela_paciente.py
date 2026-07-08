import time

import FreeSimpleGUI as sg
sg.set_options(font=("Arial", 11))


class TelaPaciente:
    __OPCOES_COR_RACA = {
        "Branca": "1",
        "Preta": "2",
        "Parda": "3",
        "Amarela": "4",
        "Indígena": "5",
        "Não informar": "6",
    }

    def __init__(self):
        self.__janela_lista = None
        self.__conteudo_lista = ""
        self.__ultima_chamada = 0

    def tela_opcoes(self):
        layout = [
            [sg.Text("Gerenciar Pacientes", font=("Helvetica", 14))],
            [sg.HSeparator()],
            [sg.Button("1 - Incluir: cadastrar novo paciente", key="1", size=(40, 1))],
            [sg.Button("2 - Alterar: editar paciente já cadastrado", key="2", size=(40, 1))],
            [sg.Button("3 - Listar: exibir pacientes cadastrados", key="3", size=(40, 1))],
            [sg.Button("4 - Excluir: remover paciente do sistema", key="4", size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button("0 - Retornar ao Menu Principal", key="0", size=(40, 1))],
        ]
        window = sg.Window("Menu Pacientes", layout, modal=True)
        opcao = 0

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "0"):
                opcao = 0
                break
            if event in ("1", "2", "3", "4"):
                opcao = int(event)
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return opcao

    def pega_dados_paciente(self, operacao: str = "INCLUIR", paciente=None):
        cpf = paciente.cpf if paciente is not None else ""
        nome_civil = paciente.nome_civil if paciente is not None else ""
        nome_social = (paciente.nome_social or "") if paciente is not None else ""
        celular = paciente.celular if paciente is not None else ""
        data_nascimento = (
            paciente.data_nascimento.strftime("%d/%m/%Y")
            if paciente is not None
            else ""
        )
        pcd = paciente.pcd if paciente is not None else False
        identidade_genero = (paciente.identidade_genero or "") if paciente is not None else ""

        cor_raca_atual = "Não informar"
        if paciente is not None and paciente.cor_raca is not None:
            mapa_cor_raca = {
                "Branca": "Branca",
                "Preta": "Preta",
                "Parda": "Parda",
                "Amarela": "Amarela",
                "Indígena": "Indígena",
                "Não Informado": "Não informar",
            }
            cor_raca_atual = mapa_cor_raca.get(paciente.cor_raca.value, "Não informar")

        titulo = f"{operacao} PACIENTE"
        layout = [
            [sg.Text(titulo, font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Text("CPF (11 dígitos):")],
            [sg.Input(default_text=cpf, key="-CPF-", size=(40, 1))],
            [sg.Text("Nome Civil:")],
            [sg.Input(default_text=nome_civil, key="-NOME-CIVIL-", size=(40, 1))],
            [sg.Text("Nome Social (opcional):", font=("Helvetica", 10, "bold"))],
            [sg.Input(default_text=nome_social, key="-NOME-SOCIAL-", size=(40, 1))],
            [sg.Text("Se preenchido, este nome substitui o nome civil em todas as telas e relatórios do sistema.", font=("Helvetica", 8), text_color="#CFCFCF")],
            [sg.Text("Celular:")],
            [sg.Input(default_text=celular, key="-CELULAR-", size=(40, 1))],
            [sg.Text("Data de Nascimento (DD/MM/AAAA):")],
            [sg.Input(default_text=data_nascimento, key="-DATA-NASCIMENTO-", size=(40, 1))],
            [sg.Text("PCD?")],
            [
                sg.Radio("Sim", "PCD", key="-PCD-S-", default=pcd),
                sg.Radio("Não", "PCD", key="-PCD-N-", default=not pcd),
            ],
            [sg.Text("Cor/Raça (IBGE):")],
            [sg.Combo(
                list(self.__OPCOES_COR_RACA.keys()),
                default_value=cor_raca_atual,
                key="-COR-RACA-",
                readonly=True,
                size=(30, 1),
            )],
            [sg.Text("Identidade de Gênero (opcional):")],
            [sg.Input(default_text=identidade_genero, key="-IDENTIDADE-GENERO-", size=(40, 1))],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window(titulo, layout, modal=True)
        dados = {
            "cpf": "",
            "nome_civil": "",
            "nome_social": None,
            "celular": "",
            "data_nascimento": "",
            "pcd": False,
            "cor_raca_opcao": "6",
            "identidade_genero": "Prefiro não responder",
        }

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                cor_raca = self.__OPCOES_COR_RACA.get(values["-COR-RACA-"], "6")
                dados = {
                    "cpf": values["-CPF-"].strip(),
                    "nome_civil": values["-NOME-CIVIL-"].strip(),
                    "nome_social": values["-NOME-SOCIAL-"].strip() or None,
                    "celular": values["-CELULAR-"].strip(),
                    "data_nascimento": values["-DATA-NASCIMENTO-"].strip(),
                    "pcd": values["-PCD-S-"],
                    "cor_raca_opcao": str(cor_raca),
                    "identidade_genero": values["-IDENTIDADE-GENERO-"].strip() or "Prefiro não responder",
                }
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return dados

    def mostra_paciente(self, paciente):
        agora = time.time()
        self.__processa_janela_lista()
        # T2: separa chamadas de listagem diferentes sem abrir uma janela por item.
        if self.__janela_lista is None or (agora - self.__ultima_chamada) > 0.5:
            self.__conteudo_lista = ""
            layout = [[sg.Multiline(
                key="-LISTA-",
                size=(60, 20),
                disabled=True,
                autoscroll=True,
                font=("Courier New", 10),
            )]]
            self.__janela_lista = sg.Window("Lista de Pacientes", layout, finalize=True)
        self.__ultima_chamada = agora

        data_str = paciente.data_nascimento
        if hasattr(data_str, "strftime"):
            data_str = data_str.strftime("%d/%m/%Y")

        linhas = [
            f"CPF: {paciente.cpf}",
            f"Celular: {paciente.celular}",
            f"Idade: {paciente.idade} anos (Nascimento: {data_str})",
            f"PCD: {'Sim' if paciente.pcd else 'Não'}",
        ]
        if paciente.cor_raca:
            linhas.append(f"Cor/Raça: {paciente.cor_raca.value}")
        if paciente.identidade_genero:
            linhas.append(f"Gênero: {paciente.identidade_genero}")
        if paciente.responsavel:
            linhas.append(f"Responsável Legal: {paciente.responsavel.nome}")
        linhas.append("-" * 40)

        lista = self.__janela_lista["-LISTA-"]
        lista.print(linhas[0])
        lista.print(f"Nome: {paciente.nome}", font=("Courier New", 10, "bold"))
        for linha in linhas[1:]:
            lista.print(linha)
        self.__janela_lista.refresh()

    def seleciona_paciente(self) -> str:
        layout = [
            [sg.Text("CPF do paciente:")],
            [sg.Input(key="-CPF-", size=(30, 1), focus=True)],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Selecionar Paciente", layout, modal=True)
        cpf = ""

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                cpf = values["-CPF-"].strip()
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return cpf

    def confirma_atualizar_responsavel(self, nome_responsavel: str, nome_paciente: str) -> bool:
        layout = [
            [sg.Text(f"Deseja também atualizar os dados do responsável {nome_responsavel} (responsável de {nome_paciente})?")],
            [sg.Button("Sim", key="-SIM-"), sg.Button("Não", key="-NAO-")],
        ]
        window = sg.Window("SisClínica - Pacientes", layout, modal=True)

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "-NAO-"):
                window.close()
                return False
            if event == "-SIM-":
                window.close()
                return True

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClínica - Pacientes")

    def __processa_janela_lista(self):
        if self.__janela_lista is None:
            return
        event, _ = self.__janela_lista.read(timeout=0)
        if event == sg.WIN_CLOSED:
            self.__janela_lista.close()
            self.__janela_lista = None
