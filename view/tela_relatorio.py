# T2: FreeSimpleGUI — biblioteca leve, sem dependência externa
import FreeSimpleGUI as sg
sg.set_options(font=("Arial", 11))


class TelaRelatorios:

    def tela_opcoes(self):
        layout = [
            [sg.Text("RELATÓRIOS E INDICADORES", font=("Arial", 12, "bold"), justification="center", expand_x=True)],
            [sg.Button("1 - Clínicas com mais atendimentos", key="1", size=(40, 1), tooltip="Clínicas com maior número de atendimentos")],
            [sg.Button("2 - Atendimentos mais caros/baratos", key="2", size=(40, 1), tooltip="Atendimentos mais caros e mais baratos")],
            [sg.Button("3 - Procedimentos mais realizados", key="3", size=(40, 1), tooltip="Procedimentos mais realizados (populares)")],
            [sg.Button("4 - Procedimentos mais caros/baratos", key="4", size=(40, 1), tooltip="Procedimentos mais caros e mais baratos")],
            [sg.Button("0 - Voltar", key="0", size=(40, 1), tooltip="Retornar ao Menu Principal")],
        ]
        window = sg.Window("Relatórios e Indicadores", layout, modal=True)
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
        window = sg.Window("Relatório Emitido", layout, modal=True)

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "-FECHAR-"):
                break

        window.close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="SisClínica - Relatórios")
