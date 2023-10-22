from entidade.boi import Boi
from limite.tela_boi import TelaBoi
from exceptions.ListaVaziaException import BoiException
from exceptions.JaExisteException import BoiJaExisteException


class ControladorBoi:

    def __init__(self, controlador_sistema):
        self.__tela_boi = TelaBoi()
        self.__controlador_sistema = controlador_sistema
        self.__bois = []

    def pega_boi_num(self, num_boi: int):
        for boi in self.__bois:
            if boi.num_boi == num_boi:
                return boi
        return None

    def lista_bois(self):
        try:
            if len(self.__bois) != 0:
                for boi in self.__bois:
                    self.__tela_boi.lista_bois({"num": boi.num_boi, "parte": boi.parte, "peso": boi.peso})
            else:
                raise BoiException
        except BoiException as e:
            self.__tela_boi.mostra_mensagem('\n')
            self.__tela_boi.mostra_mensagem(e)
            self.__tela_boi.mostra_mensagem('\n')

    def lista_partes(self):
        self.__tela_boi.mostra_mensagem('As partes do boi são: dianteiro e traseiro')

    def cria_boi(self):
        dados = self.__tela_boi.pega_dados()
        boi = self.pega_boi_num(dados['num'])
        try:
            if boi is None:
                boi = Boi(dados["num"], dados["parte"], dados["peso"])
                self.__bois.append(boi)
                self.__tela_boi.mostra_mensagem('Boi adicionado ao estoque')

            else:
                raise BoiJaExisteException
        except BoiJaExisteException as e:
            self.__tela_boi.mostra_mensagem(e)

    def alterar(self):
        self.lista_bois()
        num_boi = self.__tela_boi.seleciona_boi()
        boi = self.pega_boi_num(num_boi)
        if boi is not None:
            novos_dados = self.__tela_boi.pega_dados()
            boi.num_boi = novos_dados["num_boi"]
            boi.parte = novos_dados["parte"]
            boi.peso = novos_dados["peso"]
            self.lista_bois()

        else:
            self.__tela_boi.mostra_mensagem('Boi não está no estoque')

    def excluir(self):
        self.lista_bois()
        num_boi = self.__tela_boi.seleciona_boi()
        boi = self.pega_boi_num(num_boi)

        if boi is not None:
            self.__bois.remove(boi)
            self.__tela_boi.mostra_mensagem('Boi removido do estoque')
            self.lista_bois()

        else:
            self.__tela_boi.mostra_mensagem('Boi não encontrado no estoque')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_boi, 2: self.alterar,
                        3: self.excluir, 4: self.lista_bois,
                        5: self.lista_partes, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_boi.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
