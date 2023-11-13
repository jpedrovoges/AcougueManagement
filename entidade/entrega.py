from entidade.cliente import Cliente
from entidade.estoque import Estoque



class Entrega:
    def __init__(self, cpf_cliente: Cliente.cpf, cod: int):
        self.__cpf_cliente = cpf_cliente
        self.__cod = cod
        self.__carnes = []

    @property
    def carnes(self):
        return self.__carnes

    @property
    def cliente(self):
        return self.__cpf_cliente

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod):
        self.__cod = cod
