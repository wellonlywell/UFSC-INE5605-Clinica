import tkinter as tk
from tkinter import messagebox

_ROOT = None  # T2: raiz tkinter escondida, compartilhada pelas janelas


def _get_root():
    global _ROOT
    if _ROOT is None:
        _ROOT = tk.Tk()
        _ROOT.withdraw()
    return _ROOT


class TelaSistema:

    def tela_opcoes(self):
        janela = tk.Toplevel(_get_root())
        janela.title("SisClínica")
        janela.geometry("320x420")
        janela.grab_set()
        resultado = {"opcao": 0}

        def escolher(opcao):
            resultado["opcao"] = opcao
            janela.destroy()

        tk.Label(janela, text="SisClínica", font=("Arial", 16, "bold")).pack(pady=10)

        opcoes = [
            (1, "Gerenciar Clínicas"),
            (2, "Gerenciar Profissionais"),
            (3, "Gerenciar Tipos de Atendimento"),
            (4, "Gerenciar Procedimentos"),
            (5, "Gerenciar Pacientes"),
            (6, "Gerenciar Atendimentos"),
            (7, "Gerenciar Pagamentos"),
            (8, "Emitir Relatórios"),
        ]
        for numero, texto in opcoes:
            tk.Button(janela, text=f"{numero} - {texto}", width=35,
                      command=lambda n=numero: escolher(n)).pack(pady=3)

        tk.Button(janela, text="0 - Sair", width=35, bg="#e74c3c", fg="white",
                  command=lambda: escolher(0)).pack(pady=(15, 10))

        janela.protocol("WM_DELETE_WINDOW", lambda: escolher(0))
        janela.wait_window()
        return resultado["opcao"]

    def mostra_mensagem(self, mensagem: str):
        messagebox.showinfo("SisClínica", mensagem)