import tkinter as tk
from tkinter import messagebox
import time

_ROOT = None  # T2: raiz tkinter escondida, compartilhada pelas janelas


def _get_root():
    global _ROOT
    if _ROOT is None:
        _ROOT = tk.Tk()
        _ROOT.withdraw()
    return _ROOT


class TelaCatalogoProcedimento:

    def __init__(self):
        self.__janela_lista = None
        self.__texto_lista = None
        self.__ultima_chamada = 0

    def tela_opcoes(self):
        janela = tk.Toplevel(_get_root())
        janela.title("Menu Catálogo de Procedimentos")
        janela.grab_set()
        resultado = {"opcao": 0}

        def escolher(opcao):
            resultado["opcao"] = opcao
            janela.destroy()

        tk.Label(janela, text="CATÁLOGO DE PROCEDIMENTOS", font=("Arial", 12, "bold")).pack(pady=8)
        tk.Button(janela, text="1 - Incluir", width=30, command=lambda: escolher(1)).pack(pady=2)
        tk.Button(janela, text="2 - Alterar", width=30, command=lambda: escolher(2)).pack(pady=2)
        tk.Button(janela, text="3 - Listar", width=30, command=lambda: escolher(3)).pack(pady=2)
        tk.Button(janela, text="4 - Excluir", width=30, command=lambda: escolher(4)).pack(pady=2)
        tk.Button(janela, text="0 - Voltar", width=30, command=lambda: escolher(0)).pack(pady=(2, 8))

        janela.protocol("WM_DELETE_WINDOW", lambda: escolher(0))
        janela.wait_window()
        return resultado["opcao"]

    def pega_dados_procedimento(self):
        janela = tk.Toplevel(_get_root())
        janela.title("Dados do Procedimento")
        janela.grab_set()

        tk.Label(janela, text="Descrição (Ex: Hemograma, Curativo):").pack(anchor="w", padx=10)
        entrada_descricao = tk.Entry(janela, width=40)
        entrada_descricao.pack(padx=10, pady=2)

        tk.Label(janela, text="Custo em R$ (Ex: 150.50):").pack(anchor="w", padx=10)
        entrada_custo = tk.Entry(janela, width=40)
        entrada_custo.pack(padx=10, pady=2)

        erro_label = tk.Label(janela, text="", fg="red")
        erro_label.pack(padx=10)

        resultado = {}

        def confirmar():
            descricao = entrada_descricao.get().strip()
            if not descricao:
                erro_label.config(text="A descrição não pode ficar em branco.")
                return
            try:
                custo = float(entrada_custo.get().strip().replace(",", "."))
            except ValueError:
                erro_label.config(text="Digite um valor numérico válido para o custo.")
                return
            if custo <= 0:
                erro_label.config(text="O custo deve ser maior que zero.")
                return
            resultado["dados"] = {"descricao": descricao, "custo": custo}
            janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
        janela.protocol("WM_DELETE_WINDOW", janela.destroy)
        janela.wait_window()
        # T2: se cancelou (fechou sem confirmar), volta descrição vazia -> controller rejeita
        return resultado.get("dados", {"descricao": "", "custo": 0})

    def mostra_procedimento(self, procedimento):
        agora = time.time()
        if self.__janela_lista is None or (agora - self.__ultima_chamada) > 0.5:
            self.__janela_lista = tk.Toplevel(_get_root())
            self.__janela_lista.title("Lista de Procedimentos")
            self.__texto_lista = tk.Text(self.__janela_lista, width=60, height=20)
            self.__texto_lista.pack(padx=10, pady=10)
        self.__ultima_chamada = agora

        linhas = [
            f"ID: {procedimento.id}",
            f"Descrição: {procedimento.descricao}",
            f"Custo: R$ {procedimento.custo:.2f}",
            "-" * 40,
        ]
        self.__texto_lista.insert(tk.END, "\n".join(linhas) + "\n")

    def seleciona_procedimento(self) -> int:
        janela = tk.Toplevel(_get_root())
        janela.title("Selecionar Procedimento")
        janela.grab_set()

        tk.Label(janela, text="ID do procedimento (0 para cancelar):").pack(padx=10, pady=5)
        entrada = tk.Entry(janela, width=20)
        entrada.pack(padx=10, pady=5)

        resultado = {"id": 0}

        def confirmar():
            try:
                resultado["id"] = int(entrada.get().strip())
            except ValueError:
                resultado["id"] = 0
            janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
        janela.protocol("WM_DELETE_WINDOW", confirmar)
        entrada.focus()
        janela.wait_window()
        return resultado["id"]

    def mostra_mensagem(self, mensagem: str):
        messagebox.showinfo("SisClínica - Catálogo de Procedimentos", mensagem)