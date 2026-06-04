# class feita por Well

from model.pessoa import Pessoa
from model.cor_raca import CorRaca
from typing import Optional
# Exceptions customizadas, validações de dado movidas para a pasta exceptions
from exceptions.dado_invalido_exception import DadoInvalidoException

class Responsavel(Pessoa):
  def __init__(self, nome_civil: str, celular: str, cpf: str,
               parentesco: str,
               nome_social: Optional[str] = None,
               pcd: bool = False,
               cor_raca: Optional[CorRaca] = None,
               identidade_genero: Optional[str] = None):

      # Passando apenas os atributos que a Pessoa possui
      super().__init__(nome_civil, celular, cpf, nome_social, pcd, cor_raca, identidade_genero)
      self.parentesco = parentesco

  @property
  def parentesco(self) -> str:
    return self.__parentesco

  @parentesco.setter
  def parentesco(self, valor: str):
    if not isinstance(valor, str) or not valor.strip():
      raise DadoInvalidoException("Parentesco não pode ser vazio.")
    self.__parentesco = valor.strip()

  def get_info(self) -> str:
    pcd_str = "Sim" if self.pcd else "Não"
    cor = self.cor_raca.value if self.cor_raca else "Não informado"
    genero = self.identidade_genero or "Não informado"
    return (f"Responsável: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Celular: {self.celular}\n"
            f"Parentesco: {self.__parentesco}\n"
            f"PCD: {pcd_str}\n"
            f"Cor/Raça: {cor}\n"
            f"Identidade de Gênero: {genero}")

  def __str__(self) -> str:
    return f"Responsável: {self.nome} (Parentesco: {self.parentesco})"