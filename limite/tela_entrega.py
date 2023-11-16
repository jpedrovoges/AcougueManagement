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
        cpf = input("Favor informar o cpf do cliente: ")
        codigo = input('Informe o código da entrega: ')
        return {"cpf": cpf, "codigo": codigo}

    def adc_carne(self):
        carnes= {}
        preco = 0
        while True:
            self.__estoque.lista_carnes()
            cod = int(input('Digite o codigo da carne: '))
            qtd = float(input('Quantidade: '))
            if self.__estoque.pega_cod(cod) is not None:
                self.__estoque.alterar_qtd(cod, qtd)
                self.__estoque.lista_carnes()
            i = int(input('Deseja adicionar mais carnes (1-sim ou 2-não): '))
            if i == 2:
                return carnes


    def mostra_mensagem(self, msg):
        print(msg)