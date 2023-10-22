class TelaSistema:

    def tela_opcoes(self):
        print('-----------------------------------------------')
        print('------------- Açougue Maneggement -------------')
        print('-----------------------------------------------')
        print('-- Escolha uma opção:')
        print('1 - Estoque')
        print('2 - Entrega')
        print('3 - Cliente')
        print('4 - Fornecedor')
        print('5 - Açougueiro')
        print('6 - Motorista')
        print('7 - Boi')
        print('0 - Exit')
        print('\n')

        opcao = int(input('Escolha uma opção: '))
        return opcao
