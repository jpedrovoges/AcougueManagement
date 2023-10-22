class TelaAcougueiro:
    def tela_opcoes(self):
        print('---- Açougueiro ----')
        print('Escolha uma opção:')
        print('1 - Contratar')
        print('2 - Alterar')
        print('3 - Demitir')
        print('4 - Listar todos os açougueiros contratados')
        print('0 - Retornar')
        print('\n')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print("-------- DADOS AÇOUGUEIRO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")

        return {"nome": nome, "cpf": cpf}

    def lista_acoug(self, dados):
        print('Nome: ', dados['nome'])
        print('CPF: ', dados['cpf'])
        print('\n')

    def seleciona_acoug(self):
        cpf = input('Digite o cpf do açougueiro que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)