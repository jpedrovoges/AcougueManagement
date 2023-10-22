class TelaFornecedor:

    def tela_opcoes(self):
        print('---- Fornecedor ----')
        print('Escolha a opção')
        print('1 - Cadastrar fornecedor')
        print('2 - Alterar fornecedor')
        print('3- Excluir fornecedor')
        print('4 - Listar fornecedores cadastrados')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print("-------- DADOS FORNECEDOR ----------")
        nome = input('Nome: ')
        cpf = input('CNPJ: ')
        return {"nome": nome, "cpf": cpf}

    def lista_fornecedor(self, dados):
        print('Nome: ', dados['nome'])
        print('CNPJ: ', dados['cpf'])
        print('\n')

    def seleciona_fornecedor(self):
        cpf = input('Digite o cnpj do motorista que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
