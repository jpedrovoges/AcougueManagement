from entidade.cliente import Cliente
from entidade.estoque import Estoque



class Entrega:
    def __init__(self, cliente: Cliente, cod: int):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__cod = cod
        self.__carnes = []

    @property
    def carnes(self):
        return self.__carnes

    @property
    def cliente(self):
        return self.__cliente

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod):
        self.__cod = cod
