from typing import Type

from limite.tela_motorista import TelaMotorista
from entidade.motorista import Motorista
from exceptions.JaExisteException import MotoristaJaExisteException
from exceptions.ListaVaziaException import ListaVaziaException


class ControladorMotorista:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__motoristas = []
        self.__tela_motorista = TelaMotorista()

    def pega_motora_cpf(self, cpf: int):
        for motorista in self.__motoristas:
            if motorista.cpf == cpf:
                return motorista
        return None

    def lista_motoristas(self):
        try:
            if len(self.__motoristas) != 0:
                for motorista in self.__motoristas:
                    self.__tela_motorista.lista_motora({"nome": motorista.nome, "cpf": motorista.cpf})
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_motorista.mostra_mensagem(e)
            self.__tela_motorista.mostra_mensagem('\n')

    def contratar(self):
        dados = self.__tela_motorista.pega_dados()
        motora = self.pega_motora_cpf(dados['cpf'])
        try:
            if motora is None:
                motorista = Motorista(dados['nome'], dados['cpf'])
                self.__motoristas.append(motorista)
                self.__tela_motorista.mostra_mensagem('Motorista contratado!')

            else:
                raise MotoristaJaExisteException
        except MotoristaJaExisteException as e:
            self.__tela_motorista.mostra_mensagem(e)

    def alterar(self):
        self.lista_motoristas()
        cpf = self.__tela_motorista.seleciona_motora()
        motora = self.pega_motora_cpf(cpf)

        if motora is not None:
            novos_dados = self.__tela_motorista.pega_dados()
            motora.nome = novos_dados["nome"]
            motora.cpf = novos_dados["cpf"]
            self.lista_motoristas()
        else:
            self.__tela_motorista.mostra_mensagem('Motorista não está no quadro de funcionários')

    def demitir(self):
        self.lista_motoristas()
        cpf = self.__tela_motorista.seleciona_motora()
        motora = self.pega_motora_cpf(cpf)
        if motora is not None:
            self.__motoristas.remove(motora)
            self.__tela_motorista.mostra_mensagem('O motorista foi demitido')
            self.lista_motoristas()

        else:
            self.__tela_motorista.mostra_mensagem('Motorista não consta em nosso quadro de funcionário.')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.contratar, 2: self.alterar,
                        3: self.demitir, 4: self.lista_motoristas,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_motorista.tela_opcoes()]()
