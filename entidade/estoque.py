class Estoque:
    def __init__(self):
        self.__corte = ['Acém', 'Granito', 'Paleta', 'Maminha', 'Alcatra,'
                        'Tatu', 'Picanha', 'Contra Filé', 'Costela', 'Coxão Duro',
                        'Coxão Mole']

        self.__preco_peca = {'Acém': 19.90, 'Granito': 24.85, 'Paleta': 23.45, 'Maminha': 33.50, 'Alcatra': 29.90,
                             'Tatu': 28.70, 'Picanha': 63.90, 'Contra Filé': 32.85, 'Costela': 14.50, 'Coxão Duro': 29.90,
                             'Coxão Mole': 31.90}

        self.__qtd_peca = {'Acém': 0, 'Granito': 0, 'Paleta': 0, 'Maminha': 0, 'Alcatra': 0,
                           'Tatu': 0, 'Picanha': 0, 'Contra Filé': 0, 'Costela': 0, 'Coxão Duro': 0,
                           'Coxão Mole': 0}

    @property
    def corte(self):
        return self.__corte

    @corte.setter
    def corte(self, peca, peca_alterada):
        if peca in self.__peca:
            ind = 0
            while ind < len(self.__corte):
                if self.__corte == peca:
                    self.__corte = peca_alterada
                ind += 1

    @property
    def preco_peca(self):
        return self.__preco_peca

    @preco_peca.setter
    def preco_peca(self, peca, valor):
        if peca in self.__preco_peca.keys():
            self.__preco_peca[peca] = valor

    @property
    def qtd_peca(self):
        return self.__qtd_peca

    @qtd_peca.setter
    def qtd_peca(self, peca, qtd):
        if peca in self.__qtd_peca.keys():
            self.__qtd_peca[peca] = peca

