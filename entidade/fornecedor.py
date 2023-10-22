from entidade.pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome: str, cpf: int):
        self.__nome = nome
        self.__cpf = cpf
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
