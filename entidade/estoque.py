class Estoque:
    def __init__(self, cod: int, corte: str, preco: float, qtd: int):
        self.__cod = cod
        self.__corte = corte
        self.__preco = preco
        self.__qtd = qtd

    @property
    def cod(self):
        return self.__cod

    @property
    def corte(self):
        return self.__corte

    @property
    def preco(self):
        return self.__preco

    @property
    def qtd(self):
        return self.__qtd

    @cod.setter
    def cod(self, cod):
        self.__cod = cod

    @corte.setter
    def corte(self, corte):
        self.__corte = corte

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd
