class TelaEstoque:

    def tela_opcoes(self):
        print('---- Estoque ----')
        print('1 - Incluir corte no estoque')
        print('2 - Alterar corte no estoque')
        print('3 - Excluir corte do estoque')
        print('4 - Listar estoque')
        print('0 - Retornar')
        print('\n')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print('-------- DADOS CARNE ----------')
        cod = input('Codigo: ')
        corte = input('Corte: ')
        preco = float(input('Preço: '))
        qtd = float(input('Qtd: '))
        return {"cod": cod, "corte": corte, "preco": preco, "qtd": qtd}

    def lista_carnes(self, dados):
        print('Cod: ', dados["cod"])
        print('Corte: ', dados["corte"])
        print('Preço: ', dados["preco"])
        print('Qtd: ', dados["qtd"])
        print('\n')

    def seleciona(self):
        cod = input('Digite o cod do corte que deseja alterar: ')
        return cod

    def lista_carnes(self, dados):
        print('Cod: ', dados["cod"])
        print('Corte: ', dados["corte"])
        print('Preço: ', dados["preco"])
        print('Qtd: ', dados["qtd"])
        print('\n')

    def mostra_mensagem(self, msg):
        print(msg)
