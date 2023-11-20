class ListaVaziaException(Exception):
    def __init__(self):
        super().__init__('A lista está vazia')

class EstoqueVazioException(Exception):
    def __init__(self):
        super().__init__('O estoque está vazio')

class BoiException(Exception):
    def __init__(self):
        super().__init__('Não há bois no estoque')

class EntregaNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Essa entrega não existe")