from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor
from exceptions.ListaVaziaException import ListaVaziaException
from exceptions.JaExisteException import  FornecedorJaExisteException


class ControladorFornecedor:
    def __init__(self, controlador_sistema):
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema

    def pega_fornecedor_cpf(self, cpf: int):
        for fornecedor in self.__fornecedores:
            if fornecedor.cpf == cpf:
                return fornecedor
        return None

    def lista_fornecedor(self):
        try:
            if len(self.__fornecedores) != 0:
                for fornecedor in self.__fornecedores:
                    self.__tela_fornecedor.lista_fornecedor({"nome": fornecedor.nome, "cpf": fornecedor.cpf})
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_fornecedor.mostra_mensagem('\n')
            self.__tela_fornecedor.mostra_mensagem(e)
            self.__tela_fornecedor.mostra_mensagem('\n')

    def cadastrar(self):
        dados = self.__tela_fornecedor.pega_dados()
        fornec = self.pega_fornecedor_cpf(dados['cpf'])
        try:
            if fornec is None:
                fornecedor = Fornecedor(dados['nome'], dados['cpf'])
                self.__fornecedores.append(fornecedor)
                self.__tela_fornecedor.mostra_mensagem('Fornecedor foi cadastrado.')

            else:
                raise FornecedorJaExisteException
        except FornecedorJaExisteException as e:
            self.__tela_fornecedor.mostra_mensagem(e)

    def alterar(self):
        self.lista_fornecedor()
        cpf = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_cpf(cpf)
        if fornecedor is not None:
            novos_dados = self.__tela_fornecedor.pega_dados()
            fornecedor.nome = novos_dados["nome"]
            fornecedor.cpf = novos_dados["cpf"]
            self.lista_fornecedor()

        else:
            self.__tela_fornecedor.mostra_mensagem('Fornecedor não está cadastrado')

    def excluir(self):
        self.lista_fornecedor()
        cpf = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_cpf(cpf)

        if fornecedor is not None:
            self.__fornecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem('O fornecedor foi removido')
            self.lista_fornecedor()

        else:
            self.__tela_fornecedor.mostra_mensagem('Fornecedor não cadastrado')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar, 2: self.alterar,
                        3: self.excluir, 4: self.lista_fornecedor,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fornecedor.tela_opcoes()]()
