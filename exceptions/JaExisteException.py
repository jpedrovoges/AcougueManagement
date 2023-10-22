class AcougueiroJaExisteException(Exception):
    def __init__(self):
        super().__init__('O açougueiro já contratado')

class MotoristaJaExisteException(Exception):
    def __init__(self):
        super().__init__('O motorista já contratado')

class FornecedorJaExisteException(Exception):
    def __init__(self):
        super().__init__('O fornecedor já cadastrado')

class ClienteJaExisteException(Exception):
    def __init__(self):
        super().__init__('O cliente já cadastrado')

class BoiJaExisteException(Exception):
    def __init__(self):
<<<<<<< HEAD
        super().__init__('Boi já cadastrado')

class CorteJaExisteException(Exception):
    def __init__(self):
        super().__init__('Corte ja inserido no estoque')
=======
        super().__init__('Boi já cadastrado')
>>>>>>> 34a0697814cdba1a57426971b0668da456ff8dff
