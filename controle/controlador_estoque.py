from entidade.estoque import Estoque
from limite.tela_estoque import TelaEstoque
from exceptions.ListaVaziaException import EstoqueVazioException
from exceptions.JaExisteException import CorteJaExisteException


class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__estoque = []
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def pega_cod(self, cod: int):
        for carne in self.__estoque:
            if carne.cod == cod:
                return carne
        return None

    def lista_carnes(self):
        try:
            if len(self.__estoque) != 0:
                for carne in self.__estoque:
                    self.__tela_estoque.lista_carnes({"cod": carne.cod, "corte": carne.corte,
                                                      "preco": carne.preco, "qtd": carne.qtd})

            else:
                raise EstoqueVazioException
        except EstoqueVazioException as e:
            self.__tela_estoque.mostra_mensagem(e)

    def incluir_peca(self):
        dados = self.__tela_estoque.pega_dados()
        cod = self.pega_cod(dados['cod'])
        try:
            if cod is None:
                carne = Estoque(dados['cod'], dados['corte'], dados['preco'], dados['qtd'])
                self.__estoque.append(carne)
                self.__tela_estoque.mostra_mensagem("Seu corte foi inserido!")
            else:
                raise CorteJaExisteException
        except CorteJaExisteException as e:
            self.__tela_estoque.mostra_mensagem('\n')
            self.__tela_estoque.mostra_mensagem(e)
            self.__tela_estoque.mostra_mensagem('\n')

    def alterar(self):
        self.lista_carnes()
        cod = self.__tela_estoque.seleciona()
        corte = self.pega_cod(cod)
        if corte is not None:
            novos_dados = self.__tela_estoque.pega_dados()
            corte.cod = novos_dados["cod"]
            corte.corte = novos_dados["corte"]
            corte.preco = novos_dados["preco"]
            corte.qtd = novos_dados["qtd"]
            self.lista_carnes()

        else:
            self.__tela_estoque.mostra_mensagem('Codigo não corresponde a nenhum corte')

    def excluir_corte(self):
        self.lista_carnes()
        cod = self.__tela_estoque.seleciona()
        corte = self.pega_cod(cod)

        if corte is not None:
            self.__estoque.remove(corte)
            self.__tela_estoque.mostra_mensagem('Seu corte foi removido')

        else:
            self.__tela_estoque.mostra_mensagem('Codigo não corresponde a nenhum corte')


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_peca, 2: self.alterar,
                        3: self.excluir_corte, 4: self.lista_carnes,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes()]()




