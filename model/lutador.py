
class Lutador:

    def __init__(self, codigo_cadastro=None, peso=None, nome_lutador=None, nome=None, total_pdl=None) -> None:
        self.__codigo_cadastro = codigo_cadastro
        self.__peso = peso
        self.__nome_lutador = nome_lutador
        self.__nome = nome
        self.__total_pdl = total_pdl

    @property
    def codigo_cadastro(self):
        return self.__codigo_cadastro

    @codigo_cadastro.setter
    def codigo_cadastro(self, value):
        self.__codigo_cadastro = value

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def nome_lutador(self):
        return self.__nome_lutador

    @nome_lutador.setter
    def nome_lutador(self, value):
        self.__nome_lutador = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def total_pdl(self):
        return self.__total_pdl

    @total_pdl.setter
    def total_pdl(self, value):
        self.__total_pdl = value
