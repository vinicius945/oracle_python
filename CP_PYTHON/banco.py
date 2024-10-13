import oracledb


def conectar():
    conn = oracledb.connect(user="RM559183", password="fiap24", dsn="oracle.fiap.com.br/orcl")
    return conn


def inclui(mensagem: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO mensagem (assunto, destinatario, remetente, conteudo)
             VALUES (:1, :2, :3, :4)"""
    cursor.execute(sql, (mensagem['assunto'], mensagem['destinatario'], mensagem['remetente'], mensagem['conteudo']))
    conn.commit()
    cursor.close()
    conn.close()


def altera(mensagem: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """UPDATE mensagem
             SET assunto = :1, destinatario = :2, remetente = :3, conteudo = :4
             WHERE id = :5"""
    cursor.execute(sql, (mensagem['assunto'], mensagem['destinatario'], mensagem['remetente'], mensagem['conteudo'], mensagem['id']))
    conn.commit()
    cursor.close()
    conn.close()


def recupera(id: int) -> dict:
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM mensagem WHERE id = :1"
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {'id': row[0], 'assunto': row[1], 'destinatario': row[2], 'remetente': row[3], 'conteudo': row[4]}
    return {}


def recupera_assunto(assunto: str) -> list:
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM mensagem WHERE assunto LIKE :1"
    cursor.execute(sql, ('%' + assunto + '%',))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{'id': row[0], 'assunto': row[1], 'destinatario': row[2], 'remetente': row[3], 'conteudo': row[4]} for row in rows]


def recupera_destinatario(destinatario: str) -> list:
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM mensagem WHERE destinatario LIKE :1"
    cursor.execute(sql, ('%' + destinatario + '%',))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{'id': row[0], 'assunto': row[1], 'destinatario': row[2], 'remetente': row[3], 'conteudo': row[4]} for row in rows]

def apaga(id: int):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM mensagem WHERE id = :1"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""
