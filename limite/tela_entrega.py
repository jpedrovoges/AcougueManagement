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
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print('-------- DADOS ENTREGA --------')
        self.__cliente.lista_clientes()
        cpf = input("Favor informar o cpf do cliente: ")
        codigo = input('Informe o código da entrega: ')
        return {"cpf": cpf, "codigo": codigo}

    def mostra_entregas(self, dados):
        print('Cod: ', dados["codigo"])
        print('Cliente: ', dados["cliente"])
        print('Carne', dados["carne"])
        print('\n')

    def adc_carne(self):
        self.__estoque.lista_carnes()
        cod_carne = int(input('Digite o codigo da carne: '))
        return cod_carne

    def seleciona(self):
        cod = input('Digite o cod da entrega que deseja alterar: ')
        return cod


    def mostra_mensagem(self, msg):
        print(msg)
