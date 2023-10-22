from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    def nome(self):
        pass


    @property
    def cpf(self):
        pass
