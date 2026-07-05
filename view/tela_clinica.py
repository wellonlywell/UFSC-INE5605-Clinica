import FreeSimpleGUI as sg


class TelaClinica:

    def tela_opcoes(self) -> int:
        """Exibe o menu de clínicas e retorna a opção escolhida (0–7)."""
        layout = [
            [sg.Text('Gerenciar Clínicas', font=('Helvetica', 14))],
            [sg.HSeparator()],
            [sg.Button('1 - Incluir: Registrar Clínica',          key='1', size=(40, 1))],
            [sg.Button('2 - Alterar: Dados de uma Clínica',        key='2', size=(40, 1))],
            [sg.Button('3 - Listar: Clínicas',                     key='3', size=(40, 1))],
            [sg.Button('4 - Excluir: Clínica',                     key='4', size=(40, 1))],
            [sg.Button('5 - Vincular Profissional à Clínica',      key='5', size=(40, 1))],
            [sg.Button('6 - Remover Profissional da Clínica',      key='6', size=(40, 1))],
            [sg.Button('7 - Listar Profissionais da Clínica',      key='7', size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button('0 - Retornar ao Menu Principal', key='0', size=(40, 1))],
        ]
        window = sg.Window('Clínicas', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                window.close()
                return 0
            if event in ('1', '2', '3', '4', '5', '6', '7'):
                window.close()
                return int(event)

    def pega_dados_clinica(self, clinica=None) -> dict:
        """Abre formulário para inserir ou alterar os dados de uma clínica.
        Retorna dict com as chaves esperadas pelo controlador.
        Em caso de cancelamento, retorna dict com valores vazios.
        """
        nome = clinica.nome if clinica is not None else ''
        cnpj = clinica.cnpj if clinica is not None else ''
        cidade = clinica.cidade if clinica is not None else ''
        descricao = clinica.descricao if clinica is not None else ''
        horario_abertura = clinica.horario_abertura.strftime('%H:%M') if clinica is not None else ''
        horario_fechamento = clinica.horario_fechamento.strftime('%H:%M') if clinica is not None else ''

        layout = [
            [sg.Text('Dados da Clínica', font=('Helvetica', 12))],
            [sg.Text('Nome Fantasia:',          size=(28, 1)), sg.Input(default_text=nome,               key='nome',               size=(30, 1))],
            [sg.Text('CNPJ (14 dígitos):',      size=(28, 1)), sg.Input(default_text=cnpj,               key='cnpj',               size=(30, 1))],
            [sg.Text('Cidade:',                 size=(28, 1)), sg.Input(default_text=cidade,             key='cidade',             size=(30, 1))],
            [sg.Text('Descrição:',              size=(28, 1)), sg.Input(default_text=descricao,          key='descricao',          size=(30, 1))],
            [sg.Text('Horário de Abertura (HH:MM):', size=(28, 1)), sg.Input(default_text=horario_abertura,   key='horario_abertura',   size=(10, 1))],
            [sg.Text('Horário de Fechamento (HH:MM):', size=(28, 1)), sg.Input(default_text=horario_fechamento, key='horario_fechamento', size=(10, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Inserir / Alterar Clínica', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {
                    'nome': '', 'cnpj': '', 'cidade': '', 'descricao': '',
                    'horario_abertura': '', 'horario_fechamento': ''
                }
            if event == 'Confirmar':
                window.close()
                return {
                    'nome':               values['nome'].strip(),
                    'cnpj':               values['cnpj'].strip(),
                    'cidade':             values['cidade'].strip(),
                    'descricao':          values['descricao'].strip(),
                    'horario_abertura':   values['horario_abertura'].strip(),
                    'horario_fechamento': values['horario_fechamento'].strip(),
                }

    def mostra_clinica(self, clinica):
        """Exibe os dados de uma clínica em uma janela popup."""
        texto = (
            f"CNPJ:               {clinica.cnpj}\n"
            f"Nome:               {clinica.nome}\n"
            f"Cidade:             {clinica.cidade}\n"
            f"Descrição:          {clinica.descricao}\n"
            f"Horário de Abertura:    {clinica.horario_abertura.strftime('%H:%M')}\n"
            f"Horário de Fechamento:  {clinica.horario_fechamento.strftime('%H:%M')}\n"
        )
        sg.popup_scrolled(texto, title='Clínica')

    def seleciona_clinica(self) -> str:
        """Abre janela para o usuário digitar o CNPJ da clínica desejada.
        Retorna a string digitada, ou '' se cancelar.
        """
        layout = [
            [sg.Text('Digite o CNPJ da clínica:')],
            [sg.Input(key='cnpj', size=(20, 1))],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Selecionar Clínica', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return ''
            if event == 'OK':
                window.close()
                return values['cnpj'].strip()

    def seleciona_profissional(self) -> str:
        """Abre janela para o usuário digitar o CPF do profissional desejado.
        Retorna a string digitada, ou '' se cancelar.
        """
        layout = [
            [sg.Text('Digite o CPF do profissional (11 dígitos):')],
            [sg.Input(key='cpf', size=(15, 1))],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Selecionar Profissional', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return ''
            if event == 'OK':
                window.close()
                return values['cpf'].strip()

    def mostra_profissionais_da_clinica(self, clinica):
        """Exibe a lista de profissionais vinculados à clínica em um popup."""
        profissionais = clinica.profissionais
        if not profissionais:
            sg.popup(f'Nenhum profissional vinculado à clínica "{clinica.nome}".', title='Profissionais da Clínica')
            return
        linhas = [f'Profissionais da clínica: {clinica.nome}\n']
        for prof in profissionais:
            linhas.append(
                f"CPF: {prof.cpf}\n"
                f"Nome: {prof.nome}\n"
                f"Especialidade: {prof.especialidade}\n"
                f"{'─' * 40}"
            )
        sg.popup_scrolled('\n'.join(linhas), title='Profissionais da Clínica')

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem ao usuário em uma janela popup."""
        sg.popup(mensagem, title='Clínicas')

