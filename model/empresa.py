
class Empresa:

    def __init__(self, cnpj=None, nome=None) -> None:
        self.__cnpj = cnpj
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, value):
        self.__cnpj = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
