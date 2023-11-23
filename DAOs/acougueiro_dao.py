from DAOs.dao import DAO
from entidade.acougueiro import Acougueiro

class AcougueiroDAO(DAO):
    def __init__(self):
        super().__init__('acougueiro.pkl')

    def add(self, acougueiro: Acougueiro):
        if acougueiro is not None and isinstance(acougueiro, Acougueiro):
            super().add(acougueiro)

    def update(self, acougueiro: Acougueiro):
        if acougueiro is not None and isinstance(acougueiro, Acougueiro):
            super().update(acougueiro)

    def remove(self, acougueiro: Acougueiro):
        if acougueiro is not None and isinstance(acougueiro, Acougueiro):
            super().remove(acougueiro)
