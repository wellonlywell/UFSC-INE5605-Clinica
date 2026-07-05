# view/tela_pagamento.py
# Converted to FreeSimpleGUI — maintains the same public interface.
#
# NOTA sobre mostra_comprovante / seleciona_pagamento:
# mostra_comprovante é chamado tanto standalone (após registrar um pagamento, para
# confirmação imediata) quanto em loop (em listar_pagamentos, antes de selecionar).
# Para cobrir os dois casos:
#   - mostra_comprovante sempre exibe um popup imediato (o usuário vê o recibo).
#   - mostra_comprovante também acumula o texto em __comprovantes_buffer.
#   - seleciona_pagamento exibe o buffer em um campo rolável + input de índice.
# O buffer é limpo no início de tela_opcoes() para não misturar entre operações.

import FreeSimpleGUI as sg


class TelaPagamento:

    def __init__(self):
        # Buffer acumulado pelas chamadas a mostra_comprovante.
        self.__comprovantes_buffer = []

    def tela_opcoes(self) -> int:
        """Exibe o menu de pagamentos e retorna a opção escolhida (0–4)."""
        self.__comprovantes_buffer.clear()  # limpa buffer ao voltar ao menu
        layout = [
            [sg.Text('Gerenciar Pagamentos', font=('Helvetica', 14))],
            [sg.HSeparator()],
            [sg.Button('1 - Incluir: registrar pagamento',              key='1', size=(40, 1))],
            [sg.Button('2 - Alterar: corrigir data de pagamento',       key='2', size=(40, 1))],
            [sg.Button('3 - Listar: histórico de pagamentos',           key='3', size=(40, 1))],
            [sg.Button('4 - Excluir: estornar/cancelar pagamento',      key='4', size=(40, 1))],
            [sg.HSeparator()],
            [sg.Button('0 - Retornar ao Menu Principal', key='0', size=(40, 1))],
        ]
        window = sg.Window('Pagamentos', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                window.close()
                return 0
            if event in ('1', '2', '3', '4'):
                window.close()
                return int(event)

    def pega_dados_pagamento(self, valor_total_atendimento: float) -> dict:
        """Abre formulário para coletar data, valor e forma de pagamento.
        valor_total_atendimento: saldo restante a pagar (exibido como referência).
        Retorna dict com as chaves: data_pgto, valor_pago, forma_pagamento.
        Em caso de cancelamento, retorna dict com valores vazios/zero.
        """
        layout = [
            [sg.Text('Registrar Pagamento', font=('Helvetica', 12))],
            [sg.Text(f'Saldo restante: R$ {valor_total_atendimento:.2f}',
                     font=('Helvetica', 11), text_color='blue')],
            [sg.HSeparator()],
            [sg.Text('Data do pagamento (DD/MM/AAAA):', size=(30, 1)), sg.Input(key='data_pgto', size=(15, 1))],
            [sg.Text(f'Valor a pagar agora (máx. R$ {valor_total_atendimento:.2f}):', size=(35, 1)),
             sg.Input(key='valor_pago', size=(12, 1))],
            [sg.Text('Forma de Pagamento:', font=('Helvetica', 11))],
            [sg.Radio('Dinheiro', 'FORMA', key='1', default=True),
             sg.Radio('Pix',      'FORMA', key='2'),
             sg.Radio('Cartão',   'FORMA', key='3')],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Registrar Pagamento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'data_pgto': '', 'valor_pago': 0.0, 'forma_pagamento': '0'}
            if event == 'Confirmar':
                # Descobre qual forma foi selecionada
                forma = '1'
                for key in ('1', '2', '3'):
                    if values[key]:
                        forma = key
                        break
                try:
                    valor = float(values['valor_pago'].strip())
                except ValueError:
                    valor = 0.0
                window.close()
                return {
                    'data_pgto':      values['data_pgto'].strip(),
                    'valor_pago':     valor,
                    'forma_pagamento': forma,
                }

    def pega_dados_dinheiro(self, valor_pago: float) -> dict:
        """Abre janela para informar a quantia entregue em dinheiro.
        Retorna dict com a chave: quantia_entregue.
        """
        layout = [
            [sg.Text('Pagamento em Dinheiro', font=('Helvetica', 12))],
            [sg.Text(f'Valor do pagamento: R$ {valor_pago:.2f}')],
            [sg.Text(f'Quantia entregue (mínimo R$ {valor_pago:.2f}):', size=(35, 1)),
             sg.Input(key='quantia', size=(12, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Dinheiro', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'quantia_entregue': valor_pago}  # valor mínimo para não quebrar
            if event == 'Confirmar':
                try:
                    quantia = float(values['quantia'].strip())
                    window.close()
                    return {'quantia_entregue': quantia}
                except ValueError:
                    sg.popup('Digite um valor numérico válido.', title='Erro')

    def pega_dados_pix(self) -> dict:
        """Abre janela para informar o CPF do pagador (Pix).
        Retorna dict com a chave: cpf_pagador.
        """
        layout = [
            [sg.Text('Pagamento via Pix', font=('Helvetica', 12))],
            [sg.Text('CPF do pagador (11 dígitos):')],
            [sg.Input(key='cpf', size=(15, 1))],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Pix', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'cpf_pagador': ''}
            if event == 'Confirmar':
                window.close()
                return {'cpf_pagador': values['cpf'].strip()}

    def pega_dados_cartao(self) -> dict:
        """Abre janela para informar número, bandeira e tipo do cartão.
        Retorna dict com as chaves: numero_cartao, bandeira, tipo_cartao.
        """
        layout = [
            [sg.Text('Pagamento com Cartão', font=('Helvetica', 12))],
            [sg.Text('Número do cartão (13–19 dígitos):', size=(30, 1)), sg.Input(key='numero', size=(22, 1))],
            [sg.Text('Bandeira (ex: Visa, Mastercard):',  size=(30, 1)), sg.Input(key='bandeira', size=(20, 1))],
            [sg.Text('Tipo de cartão:')],
            [sg.Radio('Crédito', 'TIPO', key='credito', default=True),
             sg.Radio('Débito',  'TIPO', key='debito')],
            [sg.HSeparator()],
            [sg.Button('Confirmar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Cartão', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return {'numero_cartao': '', 'bandeira': '', 'tipo_cartao': 'CRÉDITO'}
            if event == 'Confirmar':
                tipo = 'CRÉDITO' if values['credito'] else 'DÉBITO'
                window.close()
                return {
                    'numero_cartao': values['numero'].strip(),
                    'bandeira':      values['bandeira'].strip(),
                    'tipo_cartao':   tipo,
                }

    def mostra_atendimentos_pendentes(self, atendimentos: list):
        """Exibe a lista de atendimentos disponíveis para pagamento em um popup."""
        if not atendimentos:
            sg.popup('Nenhum atendimento disponível.', title='Atendimentos')
            return
        linhas = ['Atendimentos disponíveis:\n']
        for i, at in enumerate(atendimentos):
            total = at.valor + at.calcular_total_procedimentos()
            linhas.append(f"[{i}] {at.paciente.nome} — R$ {total:.2f} — {at.data.strftime('%d/%m/%Y')}")
        sg.popup_scrolled('\n'.join(linhas), title='Atendimentos Disponíveis')

    def seleciona_atendimento(self) -> int:
        """Abre janela para o usuário digitar o índice do atendimento desejado.
        Retorna o índice inteiro, ou -1 se cancelar.
        -1 garante que a verificação de bounds no controlador trate como inválido.
        """
        layout = [
            [sg.Text('Digite o índice [número entre colchetes] do atendimento:')],
            [sg.Input(key='indice', size=(8, 1))],
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

    def pega_nova_data(self, pagamento) -> str:
        """Abre janela para o usuário digitar uma nova data de pagamento.
        Abre pré-preenchido com a data atual do pagamento.
        Retorna a string DD/MM/AAAA digitada, ou '' se cancelar.
        """
        data_atual = pagamento.data.strftime('%d/%m/%Y')
        layout = [
            [sg.Text('Nova data do pagamento (DD/MM/AAAA):')],
            [sg.Input(default_text=data_atual, key='data', size=(15, 1))],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Nova Data de Pagamento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return ''
            if event == 'OK':
                window.close()
                return values['data'].strip()


    def seleciona_pagamento(self) -> int:
        """Exibe o buffer de comprovantes acumulado e pede o índice do pagamento desejado.
        Retorna o índice inteiro, ou -1 se cancelar.
        """
        texto_lista = '\n\n'.join(self.__comprovantes_buffer) if self.__comprovantes_buffer else '(lista vazia)'
        self.__comprovantes_buffer.clear()

        layout = [
            [sg.Text('Selecionar Pagamento', font=('Helvetica', 12))],
            [sg.Multiline(texto_lista, size=(70, 10), disabled=True, autoscroll=True)],
            [sg.Text('Índice []:'), sg.Input(key='indice', size=(8, 1))],
            [sg.HSeparator()],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Selecionar Pagamento', layout)
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

    def mostra_comprovante(self, texto: str):
        """Exibe o comprovante em um popup scrolled E o acumula no buffer interno
        para uso posterior em seleciona_pagamento().
        """
        self.__comprovantes_buffer.append(texto)
        sg.popup_scrolled(texto, title='Comprovante de Pagamento')

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem ao usuário em uma janela popup."""
        sg.popup(mensagem, title='Pagamentos')

