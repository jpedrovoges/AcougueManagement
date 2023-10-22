class TelaEntrega:

    def tela_opcoes(self):
        print('---- Entregas ----')
        print('Escolha uma opção: ')
        print('1 - Criar entrega')
        print('2 - Excluir entrega')
        print('3 - Cliente que mais comprou')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def criar_entrega(self):
        pedido = {}
        entrega = input("Deseja iniciar uma entrega? 1: sim, 2: nao: ")
        if entrega == 1:
            cliente = input("Favor informar o nome do cliente: ")
            continuar = True
            teste = []
            while continuar:
                corte = input('Digite o corte: ')
                qtd = float(input('Agora a qtd: '))
                pedido[corte] = qtd
                pergunta = input('Deseja inserir mais carne ao pedido? 1: sim, 2: nao: ')
                if pergunta == 2:
                    continuar = False
                teste.append(cliente)
                teste.append(pedido)
            return teste
    def exlcuir_entrega(self):
            excluir = int(input('Deseja excluir uma entrega? 1: sim 2: nao: '))
            if excluir == 1:
                print(self.__entregas)
                cliente = input('Qual é o cliente: ')
                return cliente


    #def cliente_mais_comprou(self):
        #cliente = .cliente_lucro()
        #print(cliente)

    def mostra_mensagem(self, msg):
        print(msg)