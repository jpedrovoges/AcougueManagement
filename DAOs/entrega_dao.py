from DAOs.dao import DAO
from entidade.entrega import Entrega

class EntregaDAO(DAO):
    def __init__(self):
        super().__init__('entregas.pkl')

    def add(self, entrega: Entrega):
        if entrega is not None and isinstance(entrega, Entrega):
            super().add(entrega)

    def update(self, entrega: Entrega):
        if entrega is not None and isinstance(entrega, Entrega):
            super().update(entrega)

    def remove(self, entrega: Entrega):
        if entrega is not None and isinstance(entrega, Entrega):
            super().remove(entrega)