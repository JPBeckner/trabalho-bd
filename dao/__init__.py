# Importa fonte de dados
import cx_Oracle
 
class DAConexaoFactory():
 
    # Define atributos privados
    def __init__(self):
        self.__erro_con = None
 
    # Cria Factory para objetos
    @property
    def get_conexao(self):
 
        # Define conexão e fonte de dados
        con = None
 
        # Cria string de conexão Oracle
        sconexao = "user/pass@localhost/XE"
        try:
            con = cx_Oracle.connect(sconexao)
        except Exception as e:
            self.__erro_con = str(e)
   
        return con
  
    # Retorna Erros
    @property
    def get_erros(self):
        return self.__erro_con
