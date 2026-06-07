from view.tela_relatorio import TelaRelatorios

class ControladorRelatorios:
    """
    CORREÇÃO: A versão original referenciava 'controlador_procedimento' que não existe
    no sistema. O nome correto é 'controlador_catalogo_procedimento'.
    Além disso, as opções 1 e 2 eram apenas placeholders. Agora estão implementadas.
    """

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorios()

    def abre_tela(self):
        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            if opcao == 1:
                self.relatorio_clinicas_por_atendimentos()
            elif opcao == 2:
                self.relatorio_atendimentos_caros_baratos()
            elif opcao == 3:
                self.relatorio_procedimentos_mais_realizados()
            elif opcao == 4:
                self.relatorio_procedimentos_caros_baratos()
            elif opcao == 0:
                break

    # ------------------------------------------------------------------ #
    #  Relatório 1 — Clínicas com maior número de atendimentos            #
    # ------------------------------------------------------------------ #
    def relatorio_clinicas_por_atendimentos(self):
        """
        Conta quantos atendimentos cada clínica tem.
        Usa um dicionário: chave = nome da clínica, valor = contagem.
        """
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado.")
            return

        contagem = {}
        for at in atendimentos:
            nome = at.clinica.nome
            if nome not in contagem:
                contagem[nome] = 0
            contagem[nome] += 1

        # Ordena do maior para o menor
        ranking = sorted(contagem.items(), key=lambda par: par[1], reverse=True)

        linhas = ["CLÍNICAS COM MAIOR NÚMERO DE ATENDIMENTOS\n"]
        linhas.append(f"{'Pos':<5} {'Clínica':<30} {'Atendimentos':>12}")
        linhas.append("-" * 50)
        for pos, (nome, total) in enumerate(ranking, start=1):
            linhas.append(f"{pos:<5} {nome:<30} {total:>12}")

        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))

    # ------------------------------------------------------------------ #
    #  Relatório 2 — Atendimentos mais caros e mais baratos               #
    # ------------------------------------------------------------------ #
    def relatorio_atendimentos_caros_baratos(self):
        """Lista todos os atendimentos ordenados por valor (mais caro primeiro)."""
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado.")
            return

        ordenados = sorted(atendimentos, key=lambda at: at.valor, reverse=True)

        linhas = ["ATENDIMENTOS POR VALOR (mais caro → mais barato)\n"]
        linhas.append(f"{'Pos':<5} {'Paciente':<25} {'Clínica':<20} {'Data':<12} {'Valor':>10}")
        linhas.append("-" * 75)
        for pos, at in enumerate(ordenados, start=1):
            destaque = ""
            if pos == 1:
                destaque = "  ← MAIS CARO"
            elif pos == len(ordenados):
                destaque = "  ← MAIS BARATO"
            data_str = at.data.strftime("%d/%m/%Y")
            linhas.append(
                f"{pos:<5} {at.paciente.nome:<25} {at.clinica.nome:<20} "
                f"{data_str:<12} R$ {at.valor:>7.2f}{destaque}"
            )

        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))

    # ------------------------------------------------------------------ #
    #  Relatório 3 — Procedimentos mais realizados                        #
    # ------------------------------------------------------------------ #
    def relatorio_procedimentos_mais_realizados(self):
        """
        Conta quantas vezes cada procedimento aparece nos atendimentos.
        Usa o id do procedimento como chave do dicionário.
        """
        atendimentos = self.__controlador_sistema.controlador_atendimento.get_atendimentos()
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado.")
            return

        contagem = {}
        for at in atendimentos:
            for proc in at.procedimentos:
                # ItemProcedimento não tem id, então usamos a descrição como chave
                chave = proc.descricao
                if chave not in contagem:
                    contagem[chave] = {"nome": proc.descricao, "custo": proc.custo, "qty": 0}
                contagem[chave]["qty"] += 1

        if not contagem:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum procedimento registrado nos atendimentos."
            )
            return

        ranking = sorted(contagem.values(), key=lambda x: x["qty"], reverse=True)

        linhas = ["PROCEDIMENTOS MAIS REALIZADOS\n"]
        linhas.append(f"{'Pos':<5} {'Procedimento':<30} {'Qtd':>5} {'Custo Unit.':>12}")
        linhas.append("-" * 55)
        for pos, item in enumerate(ranking, start=1):
            linhas.append(
                f"{pos:<5} {item['nome']:<30} {item['qty']:>5}    "
                f"R$ {item['custo']:>8.2f}"
            )

        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))

    # ------------------------------------------------------------------ #
    #  Relatório 4 — Procedimentos mais caros e mais baratos              #
    # ------------------------------------------------------------------ #
    def relatorio_procedimentos_caros_baratos(self):
        """
        CORREÇÃO: A versão original referenciava self.__controlador_sistema.controlador_procedimento
        que não existe. O correto é controlador_catalogo_procedimento.
        """
        procedimentos = self.__controlador_sistema.controlador_catalogo_procedimento.get_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem("Nenhum procedimento cadastrado.")
            return

        ordenados = sorted(procedimentos, key=lambda p: p.custo, reverse=True)

        linhas = ["PROCEDIMENTOS POR CUSTO (mais caros → mais baratos)\n"]
        linhas.append(f"{'Pos':<5} {'Procedimento':<35} {'Custo':>10}")
        linhas.append("-" * 53)
        for pos, proc in enumerate(ordenados, start=1):
            destaque = ""
            if pos == 1:
                destaque = "  ← MAIS CARO"
            elif pos == len(ordenados):
                destaque = "  ← MAIS BARATO"
            linhas.append(
                f"{pos:<5} {proc.descricao:<35} R$ {proc.custo:>8.2f}{destaque}"
            )

        self.__tela_relatorio.exibe_dados_relatorio("\n".join(linhas))
