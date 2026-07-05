# T2: FreeSimpleGUI — biblioteca leve, sem dependência externa
import time

import FreeSimpleGUI as sg
sg.set_options(font=("Arial", 11))


class TelaResponsavel:
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
            [sg.Text("Gerenciar Responsáveis", font=("Helvetica", 14))],
            [sg.HSeparator()],
            [sg.Button("1 - Incluir: cadastrar novo responsável", key="1", size=(40, 1))],
            [sg.Button("2 - Alterar: editar responsável já cadastrado", key="2", size=(40, 1))],
            [sg.Button("3 - Listar: exibir responsáveis cadastrados", key="3", size=(40, 1))],
            [sg.Button("4 - Excluir: remover responsável do sistema", key="4", size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button("0 - Retornar ao Menu Principal", key="0", size=(40, 1))],
        ]
        window = sg.Window("Menu Responsáveis", layout, modal=True)
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

    def pega_dados_responsavel(self, operacao: str = "INCLUIR", responsavel=None):
        cpf = responsavel.cpf if responsavel is not None else ""
        nome_civil = responsavel.nome_civil if responsavel is not None else ""
        nome_social = (responsavel.nome_social or "") if responsavel is not None else ""
        celular = responsavel.celular if responsavel is not None else ""
        parentesco = responsavel.parentesco if responsavel is not None else ""
        pcd = responsavel.pcd if responsavel is not None else False
        identidade_genero = (responsavel.identidade_genero or "") if responsavel is not None else ""

        cor_raca_atual = "Não informar"
        if responsavel is not None and responsavel.cor_raca is not None:
            mapa_cor_raca = {
                "Branca": "Branca",
                "Preta": "Preta",
                "Parda": "Parda",
                "Amarela": "Amarela",
                "Indígena": "Indígena",
                "Não Informado": "Não informar",
            }
            cor_raca_atual = mapa_cor_raca.get(responsavel.cor_raca.value, "Não informar")

        titulo = f"{operacao} RESPONSÁVEL"
        layout = [
            [sg.Text(titulo, font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Text("CPF (apenas números):")],
            [sg.Input(default_text=cpf, key="-CPF-", size=(40, 1))],
            [sg.Text("Nome Civil:")],
            [sg.Input(default_text=nome_civil, key="-NOME-CIVIL-", size=(40, 1))],
            [sg.Text("Nome Social (opcional):", font=("Helvetica", 10, "bold"))],
            [sg.Input(default_text=nome_social, key="-NOME-SOCIAL-", size=(40, 1))],
            [sg.Text("Se preenchido, este nome substitui o nome civil em todas as telas e relatórios do sistema.", font=("Helvetica", 8), text_color="#CFCFCF")],
            [sg.Text("Celular:")],
            [sg.Input(default_text=celular, key="-CELULAR-", size=(40, 1))],
            [sg.Text("Grau de Parentesco/Vínculo (Ex: Mãe, Pai, Tutor):")],
            [sg.Input(default_text=parentesco, key="-PARENTESCO-", size=(40, 1))],
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
            "parentesco": "",
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
                    "parentesco": values["-PARENTESCO-"].strip(),
                    "pcd": values["-PCD-S-"],
                    "cor_raca_opcao": str(cor_raca),
                    "identidade_genero": values["-IDENTIDADE-GENERO-"].strip() or "Prefiro não responder",
                }
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return dados

    def mostra_responsavel(self, responsavel):
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
            self.__janela_lista = sg.Window("Lista de Responsáveis", layout, finalize=True)
        self.__ultima_chamada = agora

        linhas = [
            f"CPF: {responsavel.cpf}",
            f"Nome: {responsavel.nome}",
            f"Celular: {responsavel.celular}",
            f"Parentesco/Vínculo: {responsavel.parentesco}",
            f"PCD: {'Sim' if responsavel.pcd else 'Não'}",
        ]
        if responsavel.cor_raca:
            linhas.append(f"Cor/Raça: {responsavel.cor_raca.value}")
        if responsavel.identidade_genero:
            linhas.append(f"Gênero: {responsavel.identidade_genero}")
        linhas.append("-" * 40)

        self.__conteudo_lista += "\n".join(linhas) + "\n"
        self.__janela_lista["-LISTA-"].update(self.__conteudo_lista)
        self.__janela_lista.refresh()

    def seleciona_responsavel(self) -> str:
        layout = [
            [sg.Text("CPF do responsável:")],
            [sg.Input(key="-CPF-", size=(30, 1), focus=True)],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Selecionar Responsável", layout, modal=True)
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

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClínica - Responsáveis")

    def __processa_janela_lista(self):
        if self.__janela_lista is None:
            return
        event, _ = self.__janela_lista.read(timeout=0)
        if event == sg.WIN_CLOSED:
            self.__janela_lista.close()
            self.__janela_lista = None
