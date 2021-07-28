from model.empresa import Empresa
from dao import DAConexaoFactory
 
class EmpresaDAO:
 
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
 
    def busca_empresa(self, id):
 
        # Cria instancia do objeto
        # _empresa = _empresa()
 
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
        return Empresa(*dados)
 
    def insere_empresa(self, empresa):
 
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
 
    def altera_empresa(self, empresa):
 
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
 
    def apagar_empresa(self, empresa):
 
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