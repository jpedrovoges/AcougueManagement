class TelaMotorista:
    def tela_opcoes(self):
        print('---- Motorista ----')
        print('Escolha uma opção:')
        print('1 - Contratar')
        print('2 - Alterar')
        print('3 - Demitir')
        print('4 - Listar todos os motorista contratados')
        print('0 - Retornar')
        print('\n')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print("-------- DADOS MOTORISTA ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")

        return {"nome": nome, "cpf": cpf}

    def lista_motora(self, dados):
        print('Nome: ', dados['nome'])
        print('CPF: ', dados['cpf'])
        print('\n')

    def seleciona_motora(self):
        cpf = input('Digite o cpf do motorista que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)