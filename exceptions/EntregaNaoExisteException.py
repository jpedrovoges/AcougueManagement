class EntregaNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Essa entrega não existe")