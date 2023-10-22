from limite.tela_entrega import TelaEntrega
from entidade.estoque import Estoque


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_entrega = TelaEntrega()
        self.__controlador_sistema = controlador_sistema
        self.__entrega = []

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.entregas, 2: self.excluir_entrega,
                        3: self.cliente_lucro, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_entrega.tela_opcoes()]()
