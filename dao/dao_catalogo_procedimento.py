import os
from dao.dao_base import DAOBase

_DIR_DADOS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dados")
_ARQUIVO = os.path.join(_DIR_DADOS, "catalogo_procedimentos.pkl")

class CatalogoProcedimentoDAO(DAOBase):

    def __init__(self):
        os.makedirs(_DIR_DADOS, exist_ok=True)
        super().__init__(_ARQUIVO)