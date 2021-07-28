# Importa fonte de dados
import cx_Oracle
 
class DAConexaoFactory():
 
    # Define atributos privados
 
    def __init__(self):
        self.__ORACLE = 1
        self.__erroCon = None
        self.__factory = None
 
    # Cria Factory para objetos
    def get_conexao(self, banco):
 
        # Define conexão e fonte de dados
        con = None
        self.__factory = banco
 
        # Cria string de conexão Oracle
        if (banco == self.__ORACLE):
            sconexao = "user/pass@localhost/XE"
            try:
                con = cx_Oracle.connect(sconexao)
            except Exception as e:
                self.__erroCon = str(e)
   
        return con
 
    # Retorna Erros
    def get_erros(self):
        return self.__erroCon
 
    # Retorna Factory da conexão
    def get_factory(self):
        return self.__factory
 