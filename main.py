import FreeSimpleGUI as sg
sg.set_options(icon="assets/icone_cruz_arcoiris.ico")
from control.controlador_sistema import ControladorSistema

if __name__ == "__main__":
  ControladorSistema().inicializa_sistema()
