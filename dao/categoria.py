from model.categoria import Categoria
from dao import DAConexaoFactory
 
class CategoriaDAO:
 
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
    def busca_categoria(self, id):
 
        # Cria instancia do objeto
        # categoria = categoria()
 
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
        return Categoria(*dados)
 
    def insere_categoria(self, categoria):
 
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
 
    def altera_categoria(self, categoria):
 
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
 
    def apagar_categoria(self, categoria):
 
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