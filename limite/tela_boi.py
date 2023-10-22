class TelaBoi():
    def tela_opcoes(self):
        print('----Boi----')
        print('Escolha a opção')
        print('1 - Inserir boi')
        print('2 - Alterar boi')
        print('3 - Excluir boi do estoque')
        print('4 - Bois no estoque')
        print('5 - Mostrar as partes')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print('---- DADOS BOI ----')
        num_boi = input('Número do Boi: ')
        parte = input('Parte: ')
        peso = input('Peso: ')

        return {'num': num_boi, 'parte': parte, 'peso': peso}

    def lista_bois(self, dados):
        print('Número do boi: ', dados['num'])
        print('Parte: ', dados['parte'])
        print('Peso: ', dados['peso'])
        print('\n')

    def seleciona_boi(self):
        num_boi = input('Número do boi que deseja selecionar: ')
        return num_boi

    def mostra_mensagem(self, msg):
        print(msg)