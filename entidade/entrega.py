from entidade.cliente import Cliente
from entidade.estoque import Estoque



class Entrega:
    def __init__(self):
        self.__cliente = Cliente.nome()
        self.__estoque_qtd = Estoque.qtd_peca
        self.__estoque_preco = Estoque.preco_peca
