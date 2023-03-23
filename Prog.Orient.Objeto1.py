import pyodbc

def conexao_sql():
    server = "sql-estudos.database.windows.net"
    driver = "{ODBC Driver 18 for SQL Server}"
    database = "db-estudos"
    username = "luiz.sapori@blueshift.com.br"
    port = '1433'
    Authentication = "ActiveDirectoryInteractive"
    string_conexao = 'DRIVER='+driver+';SERVER='+server+';PORT='+port+';AUTHENTICATION='+Authentication+';DATABASE='+database+';USERNAME='+username
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()


conexao_sql()
