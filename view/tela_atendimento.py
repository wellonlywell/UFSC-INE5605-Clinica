# view/tela_atendimento.py
# Converted to FreeSimpleGUI — maintains the same public interface.
#
# NOTA sobre mostra_lista_atendimento / seleciona_atendimento:
# Os controladores chamam mostra_lista_atendimento(i, at) em um for-loop e, logo
# em seguida, chamam seleciona_atendimento() para o usuário escolher um índice.
# Para evitar abrir N janelas sequenciais (uma por item da lista), usamos um
# buffer de instância (__lista_buffer): mostra_lista_atendimento acumula texto no
# buffer e seleciona_atendimento exibe tudo em uma única janela com campo de entrada.
# Quando o menu chama "3 - Listar" (sem selecionar depois), o buffer fica
# acumulado mas inofensivo — é limpo na próxima chamada a seleciona_atendimento.
# Para o caso "3 - Listar" puro, o texto aparece como popup_scrolled ao final do loop,
# pois ao retornar ao menu nada mais é chamado — ver comentário em mostra_lista_atendimento.

import FreeSimpleGUI as sg


class TelaAtendimento:

    def __init__(self):
        # Buffer acumulado pelas chamadas a mostra_lista_atendimento.
        # Contém tuplas (indice, texto_formatado).
        self.__lista_buffer = []

    def tela_opcoes(self) -> int:
        """Exibe o menu de atendimentos e retorna a opção escolhida (0–5)."""
        # Ao voltar ao menu, limpa o buffer para não misturar com a próxima listagem.
        self.__lista_buffer.clear()
        layout = [
            [sg.Text('Gerenciar Atendimentos', font=('Helvetica', 14))],
            [sg.HSeparator()],
            [sg.Button('1 - Incluir: agendar novo atendimento',       key='1', size=(40, 1))],
            [sg.Button('2 - Alterar: atualizar data/hora/valor',      key='2', size=(40, 1))],
            [sg.Button('3 - Listar: exibir todos os atendimentos',    key='3', size=(40, 1))],
            [sg.Button('4 - Excluir: cancelar atendimento',           key='4', size=(40, 1))],
            [sg.Button('5 - Registrar procedimentos realizados',      key='5', size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button('0 - Retornar ao Menu Principal', key='0', size=(40, 1))],
        ]
        window = sg.Window('Atendimentos', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                window.close()
                return 0
            if event in ('1', '2', '3', '4', '5'):
                window.close()
                return int(event)

    def pega_dados_atendimento(self) -> dict:
        """Abre formulário para cadastrar um novo atendimento.
        Retorna dict com as chaves esperadas pelo controlador.
        Em caso de cancelamento, retorna dict com valores vazios/zero.
        """
        layout = [
            [sg.Text('Novo Atendimento', font=('Helvetica', 12))],
            [sg.Text('CNPJ da Clínica (14 dígitos):',   size=(30, 1)), sg.Input(key='cnpj_clinica',    size=(20, 1))],
            [sg.Text('CPF do Paciente:',                 size=(30, 1)), sg.Input(key='cpf_paciente',    size=(15, 1))],
            [sg.Text('CPF do Profissional:',             size=(30, 1)), sg.Input(key='cpf_profissional', size=(15, 1))],
            [sg.Text('Tipo de Atendimento (descrição):', size=(30, 1)), sg.Input(key='descricao_tipo',  size=(25, 1))],
            [sg.Text('Data (DD/MM/AAAA):',               size=(30, 1)), sg.Input(key='data',            size=(15, 1))],
            [sg.Text('Hora Início (HH:MM):',             size=(30, 1)), sg.Input(key='hora_inicio',     size=(10, 1))],
            [sg.Text('Hora Fim (HH:MM):',                size=(30, 1)), sg.Input(key='hora_fim',        size=(10, 1))],
            [sg.Text('Valor Base (R$):',                 size=(30, 1)), sg.Input(key='valor',           size=(12, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Cadastrar Atendimento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {
                    'cnpj_clinica': '', 'cpf_paciente': '', 'cpf_profissional': '',
                    'descricao_tipo': '', 'data': '', 'hora_inicio': '',
                    'hora_fim': '', 'valor': 0.0,
                }
            if event == 'Confirmar':
                try:
                    valor = float(values['valor'].strip())
                except ValueError:
                    valor = 0.0
                window.close()
                return {
                    'cnpj_clinica':    values['cnpj_clinica'].strip(),
                    'cpf_paciente':    values['cpf_paciente'].strip(),
                    'cpf_profissional': values['cpf_profissional'].strip(),
                    'descricao_tipo':  values['descricao_tipo'].strip(),
                    'data':            values['data'].strip(),
                    'hora_inicio':     values['hora_inicio'].strip(),
                    'hora_fim':        values['hora_fim'].strip(),
                    'valor':           valor,
                }

    def pega_dados_alteracao(self) -> dict:
        """Abre formulário para alterar data, hora e valor de um atendimento já cadastrado.
        Retorna dict com as chaves: data, hora_inicio, hora_fim, valor.
        Em caso de cancelamento, retorna dict com valores vazios/zero.
        """
        layout = [
            [sg.Text('Alterar Atendimento', font=('Helvetica', 12))],
            [sg.Text('Nova Data (DD/MM/AAAA):',  size=(25, 1)), sg.Input(key='data',        size=(15, 1))],
            [sg.Text('Nova Hora Início (HH:MM):', size=(25, 1)), sg.Input(key='hora_inicio', size=(10, 1))],
            [sg.Text('Nova Hora Fim (HH:MM):',   size=(25, 1)), sg.Input(key='hora_fim',    size=(10, 1))],
            [sg.Text('Novo Valor Base (R$):',     size=(25, 1)), sg.Input(key='valor',       size=(12, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alterar Atendimento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'data': '', 'hora_inicio': '', 'hora_fim': '', 'valor': 0.0}
            if event == 'Confirmar':
                try:
                    valor = float(values['valor'].strip())
                except ValueError:
                    valor = 0.0
                window.close()
                return {
                    'data':        values['data'].strip(),
                    'hora_inicio': values['hora_inicio'].strip(),
                    'hora_fim':    values['hora_fim'].strip(),
                    'valor':       valor,
                }

    def mostra_atendimento(self, atendimento):
        """Exibe todos os dados de um atendimento em uma janela popup."""
        procs = atendimento.procedimentos
        if procs:
            lista_procs = '\n'.join(f"  - {p.descricao} (R$ {p.custo:.2f})" for p in procs)
        else:
            lista_procs = '  Nenhum procedimento cadastrado.'
        total = atendimento.valor + atendimento.calcular_total_procedimentos()
        texto = (
            f"Data/Hora:   {atendimento.data.strftime('%d/%m/%Y')} "
            f"das {atendimento.hora_inicio.strftime('%H:%M')} "
            f"às {atendimento.hora_fim.strftime('%H:%M')}\n"
            f"Clínica:     {atendimento.clinica.nome}\n"
            f"Paciente:    {atendimento.paciente.nome}\n"
            f"Profissional: {atendimento.profissional.nome} "
            f"(Reg.: {atendimento.profissional.registro})\n"
            f"Tipo:        {atendimento.tipo.descricao}\n"
            f"Valor Base:  R$ {atendimento.valor:.2f}\n"
            f"Procedimentos realizados:\n{lista_procs}\n"
            f"VALOR TOTAL: R$ {total:.2f}\n"
        )
        sg.popup_scrolled(texto, title='Atendimento')

    def mostra_lista_atendimento(self, indice: int, atendimento):
        """Acumula o texto do atendimento no buffer interno para exibição conjunta em
        seleciona_atendimento(). Não abre janela — a janela será aberta pela seleciona.
        Se o usuário escolher a opção '3 - Listar' (sem selecionar depois), o buffer
        será limpo quando tela_opcoes() for chamada novamente.
        """
        procs = atendimento.procedimentos
        if procs:
            lista_procs = '; '.join(f"{p.descricao} R${p.custo:.0f}" for p in procs)
        else:
            lista_procs = 'Nenhum'
        total = atendimento.valor + atendimento.calcular_total_procedimentos()
        linha = (
            f"[{indice}] {atendimento.data.strftime('%d/%m/%Y')} "
            f"{atendimento.hora_inicio.strftime('%H:%M')}–{atendimento.hora_fim.strftime('%H:%M')}  |  "
            f"Clínica: {atendimento.clinica.nome}  |  "
            f"Paciente: {atendimento.paciente.nome}  |  "
            f"Total: R$ {total:.2f}  |  Procs: {lista_procs}"
        )
        self.__lista_buffer.append(linha)

    def seleciona_atendimento(self) -> int:
        """Exibe a lista acumulada por mostra_lista_atendimento em um campo de texto
        rolável e pede ao usuário que digite o índice desejado.
        Retorna o índice inteiro, ou -1 se cancelar.
        -1 garante que __buscar_por_indice(-1) retorne None (tratado pelo controlador).
        """
        texto_lista = '\n'.join(self.__lista_buffer) if self.__lista_buffer else '(lista vazia)'
        self.__lista_buffer.clear()  # limpa para a próxima operação

        layout = [
            [sg.Text('Selecionar Atendimento', font=('Helvetica', 12))],
            [sg.Multiline(texto_lista, size=(80, 10), disabled=True, autoscroll=True)],
            [sg.Text('Índice []:'), sg.Input(key='indice', size=(8, 1))],
            [sg.HSeparator()],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Selecionar Atendimento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return -1
            if event == 'OK':
                try:
                    indice = int(values['indice'].strip())
                    window.close()
                    return indice
                except ValueError:
                    sg.popup('Digite um número inteiro válido.', title='Erro')

    def pega_id_procedimento(self) -> int:
        """Abre janela para o usuário digitar o ID do procedimento a registrar.
        Retorna o inteiro digitado, ou -1 se cancelar.
        """
        layout = [
            [sg.Text('Digite o ID do procedimento:')],
            [sg.Input(key='id', size=(10, 1))],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('ID do Procedimento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return -1
            if event == 'OK':
                try:
                    id_val = int(values['id'].strip())
                    window.close()
                    return id_val
                except ValueError:
                    sg.popup('Digite um número inteiro válido.', title='Erro')

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem ao usuário em uma janela popup."""
        sg.popup(mensagem, title='Atendimentos')

