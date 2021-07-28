
class Categoria:

    def __init__(self, nome=None, campeao=None, faixa_peso=None) -> None:
        self.__nome = nome
        self.__campeao = campeao
        self.__faixa_peso = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def campeao(self):
        return self.__campeao

    @campeao.setter
    def campeao(self, value):
        self.campeao = value

    @property
    def faixa_peso(self):
        return self.__faixa_peso

    @faixa_peso.setter
    def faixa_peso(self, value):
        self.__faixa_peso = value

