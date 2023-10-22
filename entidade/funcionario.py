from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa


class Funcionario(Pessoa, ABC):
    def __init__(self):
        pass

    @property
    def cargo(self):
        pass