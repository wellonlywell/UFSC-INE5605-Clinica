import FreeSimpleGUI as sg


class TelaSistema:

    def tela_opcoes(self) -> int:
        """Exibe o menu principal e retorna o número da opção escolhida (0–8)."""
        layout = [
            [sg.Text('SisClínica', font=('Helvetica', 18), justification='center')],
            [sg.HSeparator()],
            [sg.Button('1 - Gerenciar Clínicas',             key='1', size=(35, 1))],
            [sg.Button('2 - Gerenciar Profissionais',         key='2', size=(35, 1))],
            [sg.Button('3 - Gerenciar Tipos de Atendimento',  key='3', size=(35, 1))],
            [sg.Button('4 - Gerenciar Procedimentos',         key='4', size=(35, 1))],
            [sg.Button('5 - Gerenciar Pacientes',             key='5', size=(35, 1))],
            [sg.Button('6 - Gerenciar Atendimentos',          key='6', size=(35, 1))],
            [sg.Button('7 - Gerenciar Pagamentos',            key='7', size=(35, 1))],
            [sg.Button('8 - Emitir Relatórios',               key='8', size=(35, 1))],
            [sg.HSeparator()],
            [sg.Button('0 - Sair', key='0', size=(35, 1), button_color=('white', '#c0392b'))],
        ]
        window = sg.Window('SisClínica — Menu Principal', layout, finalize=True)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                window.close()
                return 0
            if event in ('1', '2', '3', '4', '5', '6', '7', '8'):
                window.close()
                return int(event)

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem ao usuário em uma janela popup."""
        sg.popup(mensagem, title='SisClínica')

