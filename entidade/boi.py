class Boi:
    def __init__(self, num_boi: int, parte: str, peso: float):
        self.__num_boi = num_boi
        self.__parte = parte
        self.__peso = peso

    @property
    def num_boi(self):
        return self.__num_boi

    @property
    def parte(self):
        return self.__parte

    @property
    def peso(self):
        return self.__peso

    @num_boi.setter
    def num_boi(self, num_boi):
        self.__num_boi = num_boi

    @parte.setter
    def parte(self, parte):
        self.__parte = parte

    @peso.setter
    def peso(self, peso):
        self.__peso = peso
