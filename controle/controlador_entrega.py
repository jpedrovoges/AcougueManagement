from limite.tela_entrega import TelaEntrega
from entidade.estoque import Estoque


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_entrega = TelaEntrega()
        self.__controlador_sistema = controlador_sistema
        self.__entrega = []
<<<<<<< HEAD



    def entregas(self):
        a=1

    def mostra_entrega(self):
        q=1

    def excluir_entrega(self):
        a=1

    def cliente_lucro(self):
        a=1
=======
        self.__entrega_realizada = []
        self.__cliente_lucro = {}
        self.__valor_cortes = Estoque.preco_peca
        self.__carne = Estoque.qtd_peca

    def entregas(self):
        cliente[0], pedido[1] = self.__tela_entrega.criar_entrega()
        # pedido = self.__tela_entrega.criar_entrega()

        carne = []
        qtd = []
        soma = 0

        for carnes, qtds in pedido.items():
            carne.append(carnes)
            qtd.append(qtds)

        for i in range(len(carne)):
            if carne[i] in self.__valor_cortes:
                valor = self.__valor_cortes[carne[i]]
                soma += valor * qtd[i]

        self.__cliente_lucro[cliente] += soma
        self.__entrega.append(cliente)

    def mostra_entrega(self):
        entrega = self.__entrega
        return entrega

    def excluir_entrega(self):
        cliente = TelaEntrega.exlcuir_entrega()
        try:
            if cliente in self.__entrega:
                self.__entrega.remove(cliente)
                TelaEntrega.mostra_mensagem('O cliente foi removido')
        except:
            raise EntregaNaoExisteException

    def cliente_lucro(self):
        lucro = []
        try:
            for i in sorted(self.__cliente_lucro, key=self.__cliente_lucro.get):
                lucro.append(i, self.__cliente_lucro[i])
        except:
            TelaEntrega.mostra_mensagem('Nao existe ainda.')
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.entregas, 2: self.excluir_entrega,
                        3: self.cliente_lucro, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_entrega.tela_opcoes()]()
