from entidade.cliente import Cliente
from entidade.estoque import Estoque


class Entrega:
    def __init__(self, cliente: Cliente, cod: int, carne: Estoque.corte):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__cod = cod
        self.__carne = carne

    @property
    def carne(self):
        return self.__carne

    @carne.setter
    def carne(self, carne):
        self.__carne.append(carne)

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod):
        self.__cod = cod
