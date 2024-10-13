import oracledb

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

def conectar():
    conn = oracledb.connect(user="RM559183", password="fiap24", dsn="oracle.fiap.com.br/orcl")
    return conn


def truncar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    sql = "TRUNCATE TABLE mensagem"  # Comando para truncar a tabela
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

# Executar a função para truncar a tabela mensagem
truncar_tabela()
print("Todos os dados da tebela foram apagados.")