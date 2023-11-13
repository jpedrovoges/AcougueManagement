from controle.controlador_estoque import ControladorEstoque
from controle.controlador_cliente import ControladorCliente
from controle.controlador_entrega import ControladorEntrega
from controle.controlador_fornecedor import ControladorFornecedor
from controle.controlador_acougueiro import ControladorAcougueiro
from controle.controlador_motorista import ControladorMotorista
from controle.controlador_boi import ControladorBoi
from limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_estoque = ControladorEstoque(self)
        self.__controlador_fornecedor = ControladorFornecedor(self)
        self.__controlador_acougueiro = ControladorAcougueiro(self)
        self.__controlador_motorista = ControladorMotorista(self)
        self.__controlador_boi = ControladorBoi(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_estoque(self):
        return self.__controlador_estoque

    def inicializa_sistema(self):
        self.abre_tela()

    def entrega(self):
        self.__controlador_entrega.abre_tela()
    # Chama o controlador da entrega

    def estoque(self):
        self.__controlador_estoque.abre_tela()
    # Chama o controlador do estoque

    def cliente(self):
        self.__controlador_cliente.abre_tela()
    # Chama o controlador do cliente

    def fornecedor(self):
        self.__controlador_fornecedor.abre_tela()
    # Chama o controlador do cliente

    def acougueiro(self):
        self.__controlador_acougueiro.abre_tela()
    # Chama o controlador dos açougueiros

    def motorista(self):
        self.__controlador_motorista.abre_tela()
    # Chama o controlador dos açougueiros

    def boi(self):
        self.__controlador_boi.abre_tela()
    # Chama o controlador do boi

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.estoque, 2: self.entrega,
                        3: self.cliente, 4: self.fornecedor,
                        5: self.acougueiro, 6: self.motorista,
                        7: self.boi, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

