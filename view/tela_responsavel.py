import time

import FreeSimpleGUI as sg


class TelaResponsavel:

    def __init__(self):
        self.__janela_lista = None
        self.__conteudo_lista = ""
        self.__ultima_chamada = 0

    def tela_opcoes(self):
        layout = [
            [sg.Text("MENU RESPONSAVEIS", font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Button("1 - Incluir", key="1", size=(30, 1))],
            [sg.Button("2 - Alterar", key="2", size=(30, 1))],
            [sg.Button("3 - Listar", key="3", size=(30, 1))],
            [sg.Button("4 - Excluir", key="4", size=(30, 1))],
            [sg.Button("0 - Voltar", key="0", size=(30, 1))],
        ]
        window = sg.Window("Menu Responsaveis", layout, modal=True)
        opcao = 0

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "0"):
                opcao = 0
                break
            if event in ("1", "2", "3", "4"):
                opcao = int(event)
                break

        window.close()
        return opcao

    def pega_dados_responsavel(self):
        layout = [
            [sg.Text("CPF (apenas numeros):")],
            [sg.Input(key="-CPF-", size=(40, 1))],
            [sg.Text("Nome Civil:")],
            [sg.Input(key="-NOME-CIVIL-", size=(40, 1))],
            [sg.Text("Nome Social (opcional):")],
            [sg.Input(key="-NOME-SOCIAL-", size=(40, 1))],
            [sg.Text("Celular:")],
            [sg.Input(key="-CELULAR-", size=(40, 1))],
            [sg.Text("Grau de Parentesco/Vinculo (Ex: Mae, Pai, Tutor):")],
            [sg.Input(key="-PARENTESCO-", size=(40, 1))],
            [sg.Text("PCD?")],
            [
                sg.Radio("Sim", "PCD", key="-PCD-S-", default=False),
                sg.Radio("Nao", "PCD", key="-PCD-N-", default=True),
            ],
            [sg.Text("Cor/Raca (IBGE):")],
            [sg.Combo(
                [
                    ("1", "Branca"),
                    ("2", "Preta"),
                    ("3", "Parda"),
                    ("4", "Amarela"),
                    ("5", "Indigena"),
                    ("6", "Nao informar"),
                ],
                default_value=("6", "Nao informar"),
                key="-COR-RACA-",
                readonly=True,
                size=(30, 1),
            )],
            [sg.Text("Identidade de Genero (opcional):")],
            [sg.Input(key="-IDENTIDADE-GENERO-", size=(40, 1))],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Dados do Responsavel", layout, modal=True)
        dados = {
            "cpf": "",
            "nome_civil": "",
            "nome_social": None,
            "celular": "",
            "parentesco": "",
            "pcd": False,
            "cor_raca_opcao": "6",
            "identidade_genero": "Prefiro nao responder",
        }

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                cor_raca = values["-COR-RACA-"]
                if isinstance(cor_raca, tuple):
                    cor_raca = cor_raca[0]
                dados = {
                    "cpf": values["-CPF-"].strip(),
                    "nome_civil": values["-NOME-CIVIL-"].strip(),
                    "nome_social": values["-NOME-SOCIAL-"].strip() or None,
                    "celular": values["-CELULAR-"].strip(),
                    "parentesco": values["-PARENTESCO-"].strip(),
                    "pcd": values["-PCD-S-"],
                    "cor_raca_opcao": str(cor_raca),
                    "identidade_genero": values["-IDENTIDADE-GENERO-"].strip() or "Prefiro nao responder",
                }
                break

        window.close()
        return dados

    def mostra_responsavel(self, responsavel):
        agora = time.time()
        self.__processa_janela_lista()
        if self.__janela_lista is None or (agora - self.__ultima_chamada) > 0.5:
            self.__conteudo_lista = ""
            layout = [[sg.Multiline(
                key="-LISTA-",
                size=(60, 20),
                disabled=True,
                autoscroll=True,
                font=("Courier New", 10),
            )]]
            self.__janela_lista = sg.Window("Lista de Responsaveis", layout, finalize=True)
        self.__ultima_chamada = agora

        linhas = [
            f"CPF: {responsavel.cpf}",
            f"Nome: {responsavel.nome}",
            f"Celular: {responsavel.celular}",
            f"Parentesco/Vinculo: {responsavel.parentesco}",
            f"PCD: {'Sim' if responsavel.pcd else 'Nao'}",
        ]
        if responsavel.cor_raca:
            linhas.append(f"Cor/Raca: {responsavel.cor_raca.value}")
        if responsavel.identidade_genero:
            linhas.append(f"Genero: {responsavel.identidade_genero}")
        linhas.append("-" * 40)

        self.__conteudo_lista += "\n".join(linhas) + "\n"
        self.__janela_lista["-LISTA-"].update(self.__conteudo_lista)
        self.__janela_lista.refresh()

    def seleciona_responsavel(self) -> str:
        layout = [
            [sg.Text("CPF do responsavel:")],
            [sg.Input(key="-CPF-", size=(30, 1), focus=True)],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Selecionar Responsavel", layout, modal=True)
        cpf = ""

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                cpf = values["-CPF-"].strip()
                break

        window.close()
        return cpf

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClinica - Responsaveis")

    def __processa_janela_lista(self):
        if self.__janela_lista is None:
            return
        event, _ = self.__janela_lista.read(timeout=0)
        if event == sg.WIN_CLOSED:
            self.__janela_lista.close()
            self.__janela_lista = None
