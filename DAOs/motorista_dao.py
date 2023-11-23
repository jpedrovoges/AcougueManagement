from DAOs.dao import DAO
from entidade.motorista import Motorista

class MotoristaDAO(DAO):
    def __init__(self):
        super().__init__('motorista.pkl')

    def add(self, motorista: Motorista):
        if motorista is not None and isinstance(motorista, Motorista):
            super().add(motorista)

    def update(self, motorista: Motorista):
        if motorista is not None and isinstance(motorista, Motorista):
            super().update(motorista)

    def remove(self, motorista: Motorista):
        if motorista is not None and isinstance(motorista, Motorista):
            super().remove(motorista)
