import tkinter as tk
from tkinter import messagebox

_ROOT = None  # T2: raiz tkinter escondida, compartilhada pelas janelas


def _get_root():
    global _ROOT
    if _ROOT is None:
        _ROOT = tk.Tk()
        _ROOT.withdraw()
    return _ROOT


class TelaRelatorios:

    def tela_opcoes(self):
        janela = tk.Toplevel(_get_root())
        janela.title("Relatórios e Indicadores")
        janela.grab_set()
        resultado = {"opcao": 0}

        def escolher(opcao):
            resultado["opcao"] = opcao
            janela.destroy()

        tk.Label(janela, text="RELATÓRIOS E INDICADORES", font=("Arial", 12, "bold")).pack(pady=8)
        tk.Button(janela, text="1 - Clínicas com mais atendimentos", width=40,
                  command=lambda: escolher(1)).pack(pady=2)
        tk.Button(janela, text="2 - Atendimentos mais caros/baratos", width=40,
                  command=lambda: escolher(2)).pack(pady=2)
        tk.Button(janela, text="3 - Procedimentos mais realizados", width=40,
                  command=lambda: escolher(3)).pack(pady=2)
        tk.Button(janela, text="4 - Procedimentos mais caros/baratos", width=40,
                  command=lambda: escolher(4)).pack(pady=2)
        tk.Button(janela, text="0 - Voltar", width=40, command=lambda: escolher(0)).pack(pady=(2, 8))

        janela.protocol("WM_DELETE_WINDOW", lambda: escolher(0))
        janela.wait_window()
        return resultado["opcao"]

    def exibe_dados_relatorio(self, dados_formatados: str):
        janela = tk.Toplevel(_get_root())
        janela.title("Relatório Emitido")
        janela.grab_set()

        texto = tk.Text(janela, width=80, height=25, font=("Courier", 10))
        texto.pack(padx=10, pady=10)
        texto.insert(tk.END, dados_formatados)
        texto.config(state="disabled")  # T2: só leitura, é um relatório

        tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=(0, 10))
        janela.protocol("WM_DELETE_WINDOW", janela.destroy)
        janela.wait_window()

    def mostra_mensagem(self, mensagem: str):
        messagebox.showinfo("SisClínica - Relatórios", mensagem)