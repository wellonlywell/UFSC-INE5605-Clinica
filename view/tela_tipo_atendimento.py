import FreeSimpleGUI as sg


class TelaTipoAtendimento:

    def tela_opcoes(self) -> int:
        """Exibe o menu de tipos de atendimento e retorna a opção escolhida (0–4)."""
        layout = [
            [sg.Text('Tipos de Atendimento', font=('Helvetica', 14))],
            [sg.HSeparator()],
            [sg.Button('1 - Incluir: cadastrar novo tipo',           key='1', size=(40, 1))],
            [sg.Button('2 - Alterar: editar tipo cadastrado',        key='2', size=(40, 1))],
            [sg.Button('3 - Listar: exibir tipos cadastrados',       key='3', size=(40, 1))],
            [sg.Button('4 - Excluir: remover tipo',                  key='4', size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button('0 - Retornar ao Menu Principal', key='0', size=(40, 1))],
        ]
        window = sg.Window('Tipos de Atendimento', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                window.close()
                return 0
            if event in ('1', '2', '3', '4'):
                window.close()
                return int(event)

    def pega_dados_tipo_atendimento(self, operacao: str = 'INSERIR') -> dict:
        """Abre formulário para inserir ou alterar a descrição de um tipo de atendimento.
        operacao: 'INSERIR' (padrão) ou 'ALTERAR' — afeta apenas o título da janela.
        Retorna dict com a chave 'descricao'.
        Em caso de cancelamento, retorna {'descricao': ''}.
        """
        titulo = f'{operacao} TIPO DE ATENDIMENTO'
        layout = [
            [sg.Text(titulo, font=('Helvetica', 12))],
            [sg.Text('Descrição (ex: Consulta, Retorno):')],
            [sg.Input(key='descricao', size=(35, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window(titulo, layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'descricao': ''}
            if event == 'Confirmar':
                window.close()
                return {'descricao': values['descricao'].strip()}

    def mostra_tipo_atendimento(self, tipo_atendimento):
        """Exibe os dados de um tipo de atendimento em uma janela popup."""
        texto = (
            f"ID:         {tipo_atendimento.id}\n"
            f"Descrição:  {tipo_atendimento.descricao}\n"
        )
        sg.popup_scrolled(texto, title='Tipo de Atendimento')

    def seleciona_tipo_atendimento(self) -> int:
        """Abre janela para o usuário digitar o ID do tipo de atendimento desejado.
        Retorna 0 se cancelar — o controlador trata 0 como 'cancelar' explicitamente.
        """
        layout = [
            [sg.Text('Digite o ID do tipo de atendimento (0 para cancelar):')],
            [sg.Input(key='id', size=(10, 1))],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Selecionar Tipo de Atendimento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return 0
            if event == 'OK':
                try:
                    id_val = int(values['id'].strip())
                    window.close()
                    return id_val
                except ValueError:
                    sg.popup('Digite um número inteiro válido.', title='Erro')

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem ao usuário em uma janela popup."""
        sg.popup(mensagem, title='Tipos de Atendimento')

