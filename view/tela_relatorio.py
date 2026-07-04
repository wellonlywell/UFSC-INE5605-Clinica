# T2: FreeSimpleGUI — biblioteca leve, sem dependência externa
import FreeSimpleGUI as sg


class TelaRelatorios:

    def tela_opcoes(self):
        layout = [
            [sg.Text("RELATORIOS E INDICADORES", font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Button("1 - Clinicas com mais atendimentos", key="1", size=(40, 1))],
            [sg.Button("2 - Atendimentos mais caros/baratos", key="2", size=(40, 1))],
            [sg.Button("3 - Procedimentos mais realizados", key="3", size=(40, 1))],
            [sg.Button("4 - Procedimentos mais caros/baratos", key="4", size=(40, 1))],
            [sg.Button("0 - Voltar", key="0", size=(40, 1))],
        ]
        window = sg.Window("Relatorios e Indicadores", layout, modal=True)
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

    def exibe_dados_relatorio(self, dados_formatados: str):
        layout = [
            [sg.Multiline(
                dados_formatados,
                size=(80, 25),
                font=("Courier New", 10),
                disabled=True,
                autoscroll=True,
            )],
            [sg.Button("Fechar", key="-FECHAR-")],
        ]
        window = sg.Window("Relatorio Emitido", layout, modal=True)

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "-FECHAR-"):
                break

        window.close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClinica - Relatorios")
