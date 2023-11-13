class TelaEntrega:

    def __init__(self, controlador_sistema):
        self.__cliente = controlador_sistema.controlador_cliente
        self.__estoque = controlador_sistema.controlador_estoque


    def tela_opcoes(self):
        print('---- Entregas ----')
        print('Escolha uma opção: ')
        print('1 - Criar entrega')
        print('2 - Alterar entrega')
        print('3 - Excluir entrega')
        print('4 - Listar clientes que mais compraram')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print('-------- DADOS ENTREGA --------')
        self.__cliente.lista_clientes()
        cpf_cliente = int(input("Favor informar o cpf do cliente: "))
        cod = input('Informe o código da entrega: ')
        #qtd = int(input('Digite a quantidade de carnes que deseja por: '))
        return {'cpf_cliente': cpf_cliente, 'cod': cod}


    def mostra_mensagem(self, msg):
        print(msg)