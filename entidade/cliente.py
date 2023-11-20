from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__valor = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor += valor