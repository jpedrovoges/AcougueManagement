from entidade.estoque import Estoque
from limite.tela_estoque import TelaEstoque
from exceptions.ListaVaziaException import ListaVaziaException


class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__corte = Estoque.corte
        self.__preco_peca = Estoque.preco_peca
        self.__qtd_peca = Estoque.qtd_peca
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def lista_carnes(self):
        try:
            if self.__corte == None:
                raise ListaVaziaException
            else:
                for corte in self.__corte:
                    self.__tela_estoque.lista_carnes(corte)
        except ListaVaziaException as e:
            self.__tela_estoque.mostra_mensagem(e)
            self.__tela_estoque.mostra_mensagem('\n')

    def incluir_peca(self):
        peca_nova = self.__tela_estoque.incluir_peca()
        if peca_nova not in self.__corte:
            self.__corte.append(peca_nova)
            self.__preco_peca[peca_nova] = 0
            self.__qtd_peca[peca_nova] = 0
            self.__tela_estoque.mostra_mensagem("Seu corte foi inserido!")

    def excluir_peca(self):
        peca = self.__tela_estoque.excluir_peca()
        if peca in self.__corte:
            self.__corte.remove(peca)
            self.__preco_peca.pop(peca)
            self.__qtd_peca.pop(peca)
        self.__tela_estoque.mostra_mensagem('Seu corte foi removido')

    def listar_estoque(self):
        lista_estoque = []
        cortes = self.__preco_peca.items()
        for corte, valor in cortes:
            lista_estoque += f"{corte}: R${valor:0.02f}"
        return lista_estoque

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_carnes, 2: self.incluir_peca,
                        3: self.excluir_peca, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes()]()
