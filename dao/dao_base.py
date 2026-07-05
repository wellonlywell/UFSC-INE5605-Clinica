import pickle
import os


class DAOBase:

    def __init__(self, arquivo: str):
        self.__arquivo = arquivo

    def get_all(self) -> list:
        try:
            if os.path.exists(self.__arquivo):
                with open(self.__arquivo, 'rb') as f:
                    return pickle.load(f)
        except (OSError, EOFError, pickle.UnpicklingError):
            return []
        return []

    def save_all(self, lista: list):
        with open(self.__arquivo, 'wb') as f:
            pickle.dump(lista, f)
