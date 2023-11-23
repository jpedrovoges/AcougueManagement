from DAOs.dao import DAO
from entidade.fornecedor import Fornecedor

class FornecedorDAO(DAO):
    def __init__(self):
        super().__init__('fornecedor.pkl')

    def add(self, fornecedor: Fornecedor):
        if fornecedor is not None and isinstance(fornecedor, Fornecedor):
            super().add(fornecedor)

    def update(self, fornecedor: Fornecedor):
        if fornecedor is not None and isinstance(fornecedor, Fornecedor):
            super().update(fornecedor)

    def remove(self, fornecedor: Fornecedor):
        if fornecedor is not None and isinstance(fornecedor, Fornecedor):
            super().remove(fornecedor)
