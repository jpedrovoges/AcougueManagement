from limite.tela_entrega import TelaEntrega
from entidade.entrega import Entrega
from exceptions.JaExisteException import EntregaJaExisteException


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_entrega = TelaEntrega(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__entregas = []

    def entrega_por_cod(self, cod):
        for entrega in self.__entregas:
            if entrega.cod == cod:
                return entrega
        return None

    def cria_entrega(self):
        dados_entrega = self.__tela_entrega.pega_dados()
        entreg = self.entrega_por_cod(dados_entrega["codigo"])
        try:
            cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_cpf(dados_entrega["cpf"])
            if entreg is None and cliente is not None:
                carnes = self.__tela_entrega.adc_carne()
                entrega = Entrega(cliente, dados_entrega["codigo"], carnes)
                self.__entregas.append(entrega)
                self.__tela_entrega.mostra_mensagem("Sua entrega foi incluida!")
            else:
                raise EntregaJaExisteException
        except EntregaJaExisteException as e:
            self.__tela_entrega.mostra_mensagem('\n')
            self.__tela_entrega.mostra_mensagem(e)
            self.__tela_entrega.mostra_mensagem('\n')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_entrega, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_entrega.tela_opcoes()]()
