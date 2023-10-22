from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from exceptions.ListaVaziaException import ListaVaziaException
from exceptions.JaExisteException import ClienteJaExisteException


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def lista_clientes(self):
        try:
            if len(self.__clientes) != 0:
                for cliente in self.__clientes:
                    self.__tela_cliente.lista_cliente({"nome": cliente.nome, "cpf": cliente.cpf})
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
            self.__tela_cliente.mostra_mensagem('\n')

    def cadastrar(self):
        dados = self.__tela_cliente.pega_dados()
        client = self.pega_cliente_cpf(dados['cpf'])
        try:
            if client is None:
                cliente = Cliente(dados['nome'], dados['cpf'])
                self.__clientes.append(cliente)
                self.__tela_cliente.mostra_mensagem('Cliente cadastrado.')

            else:
                raise ClienteJaExisteException
        except ClienteJaExisteException as e:
<<<<<<< HEAD
            self.__tela_cliente.mostra_mensagem('\n')
            self.__tela_cliente.mostra_mensagem(e)
            self.__tela_cliente.mostra_mensagem('\n')
=======
            self.__tela_cliente.mostra_mensagem(e)
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff

    def alterar(self):
        self.lista_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_cpf(cpf)
        if cliente is not None:
            novos_dados = self.__tela_cliente.pega_dados()
            cliente.nome = novos_dados["nome"]
            cliente.cpf = novos_dados["cpf"]
            self.lista_clientes()

        else:
            self.__tela_cliente.mostra_mensagem('Cliente não está cadastrado')

    def excluir(self):
        self.lista_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_cpf(cpf)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.__tela_cliente.mostra_mensagem('O cliente removido')
            self.lista_clientes()

        else:
            self.__tela_cliente.mostra_mensagem('Cliente não cadastrado')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar, 2: self.alterar,
                        3: self.excluir, 4: self.lista_clientes,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
