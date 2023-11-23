from DAOs.dao import DAO
from entidade.estoque import Estoque

class EstoqueDAO(DAO):
    def __init__(self):
        super().__init__('estoque.pkl')

    def add(self, estoque: Estoque):
        if estoque is not None and isinstance(estoque, Estoque):
            super().add(estoque)

    def update(self, estoque: Estoque):
        if estoque is not None and isinstance(estoque, Estoque):
            super().update(estoque)

    def remove(self, estoque: Estoque):
        if estoque is not None and isinstance(estoque, Estoque):
            super().remove(estoque)
