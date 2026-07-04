# T2: FreeSimpleGUI — biblioteca leve, sem dependência externa
import time

import FreeSimpleGUI as sg


class TelaCatalogoProcedimento:

    def __init__(self):
        self.__janela_lista = None
        self.__conteudo_lista = ""
        self.__ultima_chamada = 0

    def tela_opcoes(self):
        layout = [
            [sg.Text("CATALOGO DE PROCEDIMENTOS", font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Button("1 - Incluir", key="1", size=(30, 1))],
            [sg.Button("2 - Alterar", key="2", size=(30, 1))],
            [sg.Button("3 - Listar", key="3", size=(30, 1))],
            [sg.Button("4 - Excluir", key="4", size=(30, 1))],
            [sg.Button("0 - Voltar", key="0", size=(30, 1))],
        ]
        window = sg.Window("Menu Catalogo de Procedimentos", layout, modal=True)
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

    def pega_dados_procedimento(self):
        layout = [
            [sg.Text("Descricao (Ex: Hemograma, Curativo):")],
            [sg.Input(key="-DESCRICAO-", size=(40, 1))],
            [sg.Text("Custo em R$ (Ex: 150.50):")],
            [sg.Input(key="-CUSTO-", size=(40, 1))],
            [sg.Text("", key="-ERRO-", text_color="red", size=(45, 2))],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Dados do Procedimento", layout, modal=True)
        dados = {"descricao": "", "custo": 0}

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                descricao = values["-DESCRICAO-"].strip()
                if not descricao:
                    window["-ERRO-"].update("A descricao nao pode ficar em branco.")
                    continue
                try:
                    custo = float(values["-CUSTO-"].strip().replace(",", "."))
                except ValueError:
                    window["-ERRO-"].update("Digite um valor numerico valido para o custo.")
                    continue
                if custo <= 0:
                    window["-ERRO-"].update("O custo deve ser maior que zero.")
                    continue
                dados = {"descricao": descricao, "custo": custo}
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return dados

    def mostra_procedimento(self, procedimento):
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
            self.__janela_lista = sg.Window("Lista de Procedimentos", layout, finalize=True)
        self.__ultima_chamada = agora

        linhas = [
            f"ID: {procedimento.id}",
            f"Descricao: {procedimento.descricao}",
            f"Custo: R$ {procedimento.custo:.2f}",
            "-" * 40,
        ]
        self.__conteudo_lista += "\n".join(linhas) + "\n"
        self.__janela_lista["-LISTA-"].update(self.__conteudo_lista)
        self.__janela_lista.refresh()

    def seleciona_procedimento(self) -> int:
        layout = [
            [sg.Text("ID do procedimento (0 para cancelar):")],
            [sg.Input(key="-ID-", size=(20, 1), focus=True)],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Selecionar Procedimento", layout, modal=True)
        id_procedimento = 0

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                try:
                    id_procedimento = int(values["-ID-"].strip())
                except ValueError:
                    id_procedimento = 0
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return id_procedimento

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClinica - Catalogo de Procedimentos")

    def __processa_janela_lista(self):
        if self.__janela_lista is None:
            return
        event, _ = self.__janela_lista.read(timeout=0)
        if event == sg.WIN_CLOSED:
            self.__janela_lista.close()
            self.__janela_lista = None
