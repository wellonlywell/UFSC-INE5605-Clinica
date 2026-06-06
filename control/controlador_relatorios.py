from view.tela_relatorio import TelaRelatorios


class ControladorRelatorios:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorios()

    def abre_tela(self):
        while True:
            opcao = self.__tela_relatorio.tela_opcoes()

            if opcao == 1:
                self.__tela_relatorio.mostra_mensagem("Relatório de clínicas disponível no módulo de clínicas.")
            elif opcao == 2:
                self.__tela_relatorio.mostra_mensagem("Relatório de atendimentos disponível no módulo de atendimentos.")
            elif opcao == 3:
                self.relatorio_procedimentos_mais_realizados()
            elif opcao == 4:
                self.relatorio_procedimentos_caros_baratos()
            elif opcao == 5:
                self.__tela_relatorio.mostra_mensagem("Indicadores de equidade em desenvolvimento.")
            elif opcao == 0:
                break

    def relatorio_procedimentos_mais_realizados(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado.")
            return

        contagem = {}
        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:
                chave = procedimento.id
                if chave not in contagem:
                    contagem[chave] = {"procedimento": procedimento, "quantidade": 0}
                contagem[chave]["quantidade"] += 1

        if not contagem:
            self.__tela_relatorio.mostra_mensagem("Nenhum procedimento registrado nos atendimentos.")
            return

        ranking = sorted(contagem.values(), key=lambda x: x["quantidade"], reverse=True)
        linhas = ["PROCEDIMENTOS MAIS REALIZADOS\n"]
        for i, item in enumerate(ranking, start=1):
            proc = item["procedimento"]
            linhas.append(f"{i}. {proc.descricao} — {item['quantidade']} vez(es) | R$ {proc.custo:.2f}")
        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))

    def relatorio_procedimentos_caros_baratos(self):
        procedimentos = self.__controlador_sistema.controlador_procedimento.get_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum procedimento cadastrado.")
            return

        ranking = sorted(procedimentos, key=lambda p: p.custo, reverse=True)
        linhas = ["PROCEDIMENTOS POR CUSTO (mais caros → mais baratos)\n"]
        for i, proc in enumerate(ranking, start=1):
            linhas.append(f"{i}. {proc.descricao} — R$ {proc.custo:.2f}")
        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))