from entidade.estoque import Estoque
from limite.tela_estoque import TelaEstoque
<<<<<<< HEAD
from exceptions.ListaVaziaException import EstoqueVazioException
from exceptions.JaExisteException import CorteJaExisteException
=======
from exceptions.ListaVaziaException import ListaVaziaException
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff


class ControladorEstoque:
    def __init__(self, controlador_sistema):
<<<<<<< HEAD
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
=======
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
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
<<<<<<< HEAD
        lista_opcoes = {1: self.incluir_peca, 2: self.alterar,
                        3: self.excluir_corte, 4: self.lista_carnes,
                        0: self.retornar}
=======
        lista_opcoes = {1: self.lista_carnes, 2: self.incluir_peca,
                        3: self.excluir_peca, 0: self.retornar}
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes()]()
