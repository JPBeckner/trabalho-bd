
class Confronto:

    def __init__(
        self,
        dia_confronto=None,
        estadio=None,
        juiz=None,
        venceu_desafiante=None,
        codigo_desafiante=None,
        venceu_desafiado=None,
        codigo_desafiado=None,
    ) -> None:
        self.__dia_confronto = dia_confronto
        self.__estadio = estadio
        self.__juiz = juiz
        self.__venceu_desafiante = venceu_desafiante
        self.__codigo_desafiante = codigo_desafiante
        self.__venceu_desafiado = venceu_desafiado
        self.__codigo_desafiado = codigo_desafiado

    @property
    def dia_confronto(self):
        return self.__dia_confronto

    @dia_confronto.setter
    def dia_confronto(self, value):
        self.__dia_confronto = value

    @property
    def estadio(self):
        return self.__estadio

    @estadio.setter
    def estadio(self, value):
        self.__estadio = value

    @property
    def juiz(self):
        return self.__juiz

    @juiz.setter
    def juiz(self, value):
        self.__juiz = value

    @property
    def venceu_desafiante(self):
        return self.__venceu_desafiante

    @venceu_desafiante.setter
    def venceu_desafiante(self, value):
        self.__venceu_desafiante = value

    @property
    def codigo_desafiante(self):
        return self.__codigo_desafiante

    @codigo_desafiante.setter
    def codigo_desafiante(self, value):
        self.__codigo_desafiante = value

    @property
    def venceu_desafiado(self):
        return self.__venceu_desafiado

    @venceu_desafiado.setter
    def venceu_desafiado(self, value):
        self.__venceu_desafiado = value

    @property
    def codigo_desafiado(self):
        return self.__codigo_desafiado

    @codigo_desafiado.setter
    def codigo_desafiado(self, value):
        self.__codigo_desafiado = value
