from limite.tela_acougueiro import TelaAcougueiro
from entidade.acougueiro import Acougueiro
from exceptions.JaExisteException import AcougueiroJaExisteException
from exceptions.ListaVaziaException import ListaVaziaException


class ControladorAcougueiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__acougueiros = []
        self.__tela_acougueiro = TelaAcougueiro()

    def pega_acou_cpf(self, cpf: int):
        for acougueiro in self.__acougueiros:
            if acougueiro.cpf == cpf:
                return acougueiro
        return None

    def lista_acougueiros(self):
        try:
            if len(self.__acougueiros) != 0:
                for acougueiro in self.__acougueiros:
                    self.__tela_acougueiro.lista_acoug({"nome": acougueiro.nome, "cpf": acougueiro.cpf})
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_acougueiro.mostra_mensagem('\n')
            self.__tela_acougueiro.mostra_mensagem(e)
            self.__tela_acougueiro.mostra_mensagem('\n')

    def contratar(self):
        dados = self.__tela_acougueiro.pega_dados()
        acoug = self.pega_acou_cpf(dados['cpf'])
        try:
            if acoug == None:
                acougueiro = Acougueiro(dados['nome'], dados['cpf'])
                self.__acougueiros.append(acougueiro)
                self.__tela_acougueiro.mostra_mensagem('Açougueiro contratado!')

            else:
                raise AcougueiroJaExisteException
        except AcougueiroJaExisteException as e:
            self.__tela_acougueiro.mostra_mensagem(e)

    def alterar(self):
        self.lista_acougueiros()
        cpf = self.__tela_acougueiro.seleciona_acoug()
        acoug = self.pega_acou_cpf(cpf)

        if acoug is not None:
            novos_dados = self.__tela_acougueiro.pega_dados()
            acoug.nome = novos_dados["nome"]
            acoug.cpf = novos_dados["cpf"]
            self.lista_acougueiros()
        else:
            self.__tela_acougueiro.mostra_mensagem('Açougueiro não está no quadro de funcionários')

    def demitir(self):
        self.lista_acougueiros()
        cpf = self.__tela_acougueiro.seleciona_acoug()
        acoug = self.pega_acou_cpf(cpf)
        if acoug is not None:
            self.__acougueiros.remove(acoug)
            self.__tela_acougueiro.mostra_mensagem('O açougueiro foi demitido')
            self.lista_acougueiros()

        else:
            self.__tela_acougueiro.mostra_mensagem('Açougueiro não consta em nosso quadro de funcionário.')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.contratar, 2: self.alterar,
                        3: self.demitir, 4: self.lista_acougueiros,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_acougueiro.tela_opcoes()]()
