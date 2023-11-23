from DAOs.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):

    def __init__(self):
        super().__init__('cliente.pkl')

    def add(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente):
            super().add(cliente)

    def update(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente):
            super().update(cliente)

    def remove(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente):
            super().remove(cliente)