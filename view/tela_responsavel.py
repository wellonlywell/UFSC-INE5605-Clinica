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


class TelaResponsavel:

    def __init__(self):
        self.__janela_lista = None
        self.__texto_lista = None
        self.__ultima_chamada = 0

    def tela_opcoes(self):
        janela = tk.Toplevel(_get_root())
        janela.title("Menu Responsáveis")
        janela.grab_set()
        resultado = {"opcao": 0}

        def escolher(opcao):
            resultado["opcao"] = opcao
            janela.destroy()

        tk.Label(janela, text="MENU RESPONSÁVEIS", font=("Arial", 12, "bold")).pack(pady=8)
        tk.Button(janela, text="1 - Incluir", width=30, command=lambda: escolher(1)).pack(pady=2)
        tk.Button(janela, text="2 - Alterar", width=30, command=lambda: escolher(2)).pack(pady=2)
        tk.Button(janela, text="3 - Listar", width=30, command=lambda: escolher(3)).pack(pady=2)
        tk.Button(janela, text="4 - Excluir", width=30, command=lambda: escolher(4)).pack(pady=2)
        tk.Button(janela, text="0 - Voltar", width=30, command=lambda: escolher(0)).pack(pady=(2, 8))

        janela.protocol("WM_DELETE_WINDOW", lambda: escolher(0))
        janela.wait_window()
        return resultado["opcao"]

    def pega_dados_responsavel(self):
        janela = tk.Toplevel(_get_root())
        janela.title("Dados do Responsável")
        janela.grab_set()

        campos = {}

        def linha(label):
            tk.Label(janela, text=label).pack(anchor="w", padx=10)
            entrada = tk.Entry(janela, width=40)
            entrada.pack(padx=10, pady=2)
            return entrada

        campos["cpf"] = linha("CPF (apenas números):")
        campos["nome_civil"] = linha("Nome Civil:")
        campos["nome_social"] = linha("Nome Social (opcional):")
        campos["celular"] = linha("Celular:")
        campos["parentesco"] = linha("Grau de Parentesco/Vínculo (Ex: Mãe, Pai, Tutor):")

        pcd_var = tk.StringVar(value="N")
        tk.Label(janela, text="PCD?").pack(anchor="w", padx=10)
        frame_pcd = tk.Frame(janela)
        frame_pcd.pack(anchor="w", padx=10)
        tk.Radiobutton(frame_pcd, text="Sim", variable=pcd_var, value="S").pack(side="left")
        tk.Radiobutton(frame_pcd, text="Não", variable=pcd_var, value="N").pack(side="left")

        cor_var = tk.StringVar(value="6")
        tk.Label(janela, text="Cor/Raça (IBGE):").pack(anchor="w", padx=10)
        opcoes_cor = [("Branca", "1"), ("Preta", "2"), ("Parda", "3"),
                      ("Amarela", "4"), ("Indígena", "5"), ("Não informar", "6")]
        frame_cor = tk.Frame(janela)
        frame_cor.pack(anchor="w", padx=10)
        for texto, valor in opcoes_cor:
            tk.Radiobutton(frame_cor, text=texto, variable=cor_var, value=valor).pack(anchor="w")

        campos["identidade_genero"] = linha("Identidade de Gênero (opcional):")

        resultado = {}

        def confirmar():
            resultado["dados"] = {
                "cpf": campos["cpf"].get().strip(),
                "nome_civil": campos["nome_civil"].get().strip(),
                "nome_social": campos["nome_social"].get().strip() or None,
                "celular": campos["celular"].get().strip(),
                "parentesco": campos["parentesco"].get().strip(),
                "pcd": pcd_var.get() == "S",
                "cor_raca_opcao": cor_var.get(),
                "identidade_genero": campos["identidade_genero"].get().strip() or "Prefiro não responder",
            }
            janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
        janela.protocol("WM_DELETE_WINDOW", confirmar)
        janela.wait_window()
        return resultado.get("dados", {
            "cpf": "", "nome_civil": "", "nome_social": None, "celular": "",
            "parentesco": "", "pcd": False, "cor_raca_opcao": "6",
            "identidade_genero": "Prefiro não responder"
        })

    def mostra_responsavel(self, responsavel):
        agora = time.time()
        if self.__janela_lista is None or (agora - self.__ultima_chamada) > 0.5:
            self.__janela_lista = tk.Toplevel(_get_root())
            self.__janela_lista.title("Lista de Responsáveis")
            self.__texto_lista = tk.Text(self.__janela_lista, width=60, height=20)
            self.__texto_lista.pack(padx=10, pady=10)
        self.__ultima_chamada = agora

        linhas = [
            f"CPF: {responsavel.cpf}",
            f"Nome: {responsavel.nome}",
            f"Celular: {responsavel.celular}",
            f"Parentesco/Vínculo: {responsavel.parentesco}",
            f"PCD: {'Sim' if responsavel.pcd else 'Não'}",
        ]
        if responsavel.cor_raca:
            linhas.append(f"Cor/Raça: {responsavel.cor_raca.value}")
        if responsavel.identidade_genero:
            linhas.append(f"Gênero: {responsavel.identidade_genero}")
        linhas.append("-" * 40)

        self.__texto_lista.insert(tk.END, "\n".join(linhas) + "\n")

    def seleciona_responsavel(self) -> str:
        janela = tk.Toplevel(_get_root())
        janela.title("Selecionar Responsável")
        janela.grab_set()

        tk.Label(janela, text="CPF do responsável:").pack(padx=10, pady=5)
        entrada = tk.Entry(janela, width=30)
        entrada.pack(padx=10, pady=5)

        resultado = {"cpf": ""}

        def confirmar():
            resultado["cpf"] = entrada.get().strip()
            janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
        janela.protocol("WM_DELETE_WINDOW", confirmar)
        entrada.focus()
        janela.wait_window()
        return resultado["cpf"]

    def mostra_mensagem(self, mensagem: str):
        messagebox.showinfo("SisClínica - Responsáveis", mensagem)