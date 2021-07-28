from model.confronto import Confronto
from dao import DAConexaoFactory
 
class ConfrontoDAO:
 
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
 
    def busca_confronto(self, id):
 
        # Cria instancia do objeto
        # _confronto = _confronto()
 
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
        return Confronto(*dados)

    def busca_confronto_por_data(self, data: str):
        # exemplo de data(dia-mes-ano): "31-12-2021"
        # esta querry precisa trazer a luta referente a data correspondente
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
        return Confronto(*dados)

 
    def insere_confronto(self, confronto):
 
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
 
    def altera_confronto(self, confronto):
 
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
 
    def apagar_confronto(self, confronto):
 
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