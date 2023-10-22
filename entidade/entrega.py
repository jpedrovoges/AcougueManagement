<<<<<<< HEAD
class Entrega:
    def __init__(self):
        self.__entregas = []
=======
from entidade.cliente import Cliente
from entidade.estoque import Estoque



class Entrega:
    def __init__(self):
        self.__cliente = Cliente.nome()
        self.__estoque_qtd = Estoque.qtd_peca
        self.__estoque_preco = Estoque.preco_peca
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff
