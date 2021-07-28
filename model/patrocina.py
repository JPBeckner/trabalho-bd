
class Patrocina:

    def __init__(self, cnpj=None, codigo_cadastro=None) -> None:
        self.__cnpj = cnpj
        self.__codigo_cadastro = codigo_cadastro

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, value):
        self.__cnpj = value

    @property
    def codigo_cadastro(self):
        return self.__codigo_cadastro

    @codigo_cadastro.setter
    def codigo_cadastro(self, value):
        self.__codigo_cadastro = value
