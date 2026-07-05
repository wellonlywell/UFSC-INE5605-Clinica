# T2: FreeSimpleGUI — biblioteca leve, sem dependência externa
import time

import FreeSimpleGUI as sg
sg.set_options(font=("Arial", 11))


class TelaProfissional:
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
            [sg.Text("Gerenciar Profissionais", font=("Helvetica", 14))],
            [sg.HSeparator()],
            [sg.Button("1 - Incluir: cadastrar novo profissional", key="1", size=(40, 1))],
            [sg.Button("2 - Alterar: editar profissional já cadastrado", key="2", size=(40, 1))],
            [sg.Button("3 - Listar: exibir profissionais cadastrados", key="3", size=(40, 1))],
            [sg.Button("4 - Excluir: remover profissional do sistema", key="4", size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button("0 - Retornar ao Menu Principal", key="0", size=(40, 1))],
        ]
        window = sg.Window("Menu Profissionais", layout, modal=True)
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

    def pega_dados_profissional(self, profissional=None):
        cpf = profissional.cpf if profissional is not None else ""
        nome_civil = profissional.nome_civil if profissional is not None else ""
        nome_social = (profissional.nome_social or "") if profissional is not None else ""
        celular = profissional.celular if profissional is not None else ""
        registro = profissional.registro if profissional is not None else ""
        especialidade = profissional.especialidade if profissional is not None else ""
        pcd = profissional.pcd if profissional is not None else False
        identidade_genero = (profissional.identidade_genero or "") if profissional is not None else ""

        cor_raca_atual = "Não informar"
        if profissional is not None and profissional.cor_raca is not None:
            mapa_cor_raca = {
                "Branca": "Branca",
                "Preta": "Preta",
                "Parda": "Parda",
                "Amarela": "Amarela",
                "Indígena": "Indígena",
                "Não Informado": "Não informar",
            }
            cor_raca_atual = mapa_cor_raca.get(profissional.cor_raca.value, "Não informar")

        layout = [
            [sg.Text("CPF (11 dígitos):")],
            [sg.Input(default_text=cpf, key="-CPF-", size=(40, 1))],
            [sg.Text("Nome Civil:")],
            [sg.Input(default_text=nome_civil, key="-NOME-CIVIL-", size=(40, 1))],
            [sg.Text("Nome Social (opcional):", font=("Helvetica", 10, "bold"))],
            [sg.Input(default_text=nome_social, key="-NOME-SOCIAL-", size=(40, 1))],
            [sg.Text("Se preenchido, este nome substitui o nome civil em todas as telas e relatórios do sistema.", font=("Helvetica", 8), text_color="#CFCFCF")],
            [sg.Text("Celular:")],
            [sg.Input(default_text=celular, key="-CELULAR-", size=(40, 1))],
            [sg.Text("Registro Profissional (Ex: CRM/SC 12345, COREN 6789):")],
            [sg.Input(default_text=registro, key="-REGISTRO-", size=(40, 1))],
            [sg.Text("Especialidade Médica/Área (Ex: Clínico Geral, Pediatra):")],
            [sg.Input(default_text=especialidade, key="-ESPECIALIDADE-", size=(40, 1))],
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
        window = sg.Window("Dados do Profissional", layout, modal=True)
        dados = {
            "cpf": "",
            "nome_civil": "",
            "nome_social": None,
            "celular": "",
            "registro": "",
            "especialidade": "",
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
                    "registro": values["-REGISTRO-"].strip(),
                    "especialidade": values["-ESPECIALIDADE-"].strip(),
                    "pcd": values["-PCD-S-"],
                    "cor_raca_opcao": str(cor_raca),
                    "identidade_genero": values["-IDENTIDADE-GENERO-"].strip() or "Prefiro não responder",
                }
                break

        window.close()  # T2: fecha antes de retornar, mesmo papel do wait_window() do tkinter
        return dados

    def mostra_profissional(self, profissional):
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
            self.__janela_lista = sg.Window("Lista de Profissionais", layout, finalize=True)
        self.__ultima_chamada = agora

        linhas = [
            f"Registro Profissional: {profissional.registro}",
            f"Especialidade: {profissional.especialidade}",
            f"CPF: {profissional.cpf}",
            f"Celular: {profissional.celular}",
            f"PCD: {'Sim' if profissional.pcd else 'Não'}",
        ]
        if profissional.cor_raca:
            linhas.append(f"Cor/Raça: {profissional.cor_raca.value}")
        if profissional.identidade_genero:
            linhas.append(f"Gênero: {profissional.identidade_genero}")
        linhas.append("-" * 40)

        lista = self.__janela_lista["-LISTA-"]
        lista.print(linhas[0])
        lista.print(linhas[1])
        lista.print(f"Nome: {profissional.nome}", font=("Courier New", 10, "bold"))
        for linha in linhas[2:]:
            lista.print(linha)
        self.__janela_lista.refresh()

    def seleciona_profissional(self) -> str:
        layout = [
            [sg.Text("CPF do profissional:")],
            [sg.Input(key="-CPF-", size=(30, 1), focus=True)],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        ]
        window = sg.Window("Selecionar Profissional", layout, modal=True)
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
        sg.popup(mensagem, title="SisClínica - Profissionais")

    def __processa_janela_lista(self):
        if self.__janela_lista is None:
            return
        event, _ = self.__janela_lista.read(timeout=0)
        if event == sg.WIN_CLOSED:
            self.__janela_lista.close()
            self.__janela_lista = None
