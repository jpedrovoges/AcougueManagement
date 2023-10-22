class TelaEstoque:

    def tela_opcoes(self):
        print('---- Estoque ----')
        print('1 - Listar estoque')
        print('2 - Incluir peça do estoque')
        print('3 - Excluir peça do estoque')
        print('0 - Retornar')
        print('\n')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def lista_carnes(self, corte):
        print('Corte: ', corte)


    def mostra_mensagem(self, msg):
        print(msg)
