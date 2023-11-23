from DAOs.dao import DAO
from entidade.boi import Boi

class BoiDAO(DAO):
    def __init__(self):
        super().__init__('boi.pkl')

    def add(self, boi: Boi):
        if fornecedor is not None and isinstance(fornecedor, Boi):
            super().add(fornecedor)

    def update(self, boi: Boi):
        if boi is not None and isinstance(boi, Boi):
            super().update(boi)

    def remove(self, boi: Boi):
        if boi is not None and isinstance(boi, Boi):
            super().remove(boi)
