from model.lutador import Lutador
from dao import DAConexaoFactory
 
class LutadorDAO:
 
    # Construtor da classe
    def __init__(self):
        self.__erro = None
        self.__con = None
        try:
            conexao = DAConexaoFactory()
            self.__con = conexao.get_conexao()
        except Exception as e:
            self.__erro = str(e)
 
    # Metodo de Manipulação de dados
 
    def busca_lutador(self, id):
 
        # Cria instancia do objeto
        # _lutador = _lutador()
 
        # Define SQL
        sql = ""
 
        # Executa SQL
        try:
            cursor= self.__con.cursor()
            cursor.execute(sql)
            dados = cursor.fetchone()

        except Exception as e:
            self.__erro = str(e)
 
        # Alimenta objeto
 
        # Retorna Objeto
        return Lutador(*dados)
 
    def insere_lutador(self, lutador):
 
        # Define SQL
        sql = ""
 
        # Executa SQL
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True 
        except Exception as e:
            self.__erro = str(e)
            return False
 
    def altera_lutador(self, lutador):
 
       #  Define SQL
       sql = ""
 
       # Executa SQL
       try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True 
       except Exception as e:
           self.__erro = str(e)
           return False
 
    def apagar_lutador(self, lutador):
 
        # Define SQL
        sql = ""
 
        # Executa SQL
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True 
        except Exception as e:
            self.__erro = str(e)
            return False
 
    # Retorna Erro
    @property
    def get_erro(self):
        return self.__erro