class TelaCliente:

    def tela_opcoes(self):
        print('---- Cliente ----')
        print('Escolha a opção')
        print('1 - Cadastrar cliente')
        print('2 - Alterar cliente')
        print('3- Excluir cliente')
        print('4 - Listar clientes cadastrados')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print("-------- DADOS CLIENTES ----------")
        nome = input('Nome: ')
        cpf = input('CPF: ')
        return {"nome": nome, "cpf": cpf}

    def lista_cliente(self, dados):
        print('Nome: ', dados['nome'])
        print('CPF: ', dados['cpf'])
        print('\n')

    def seleciona_cliente(self):
        cpf = input('Digite o cpf do cliente que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
