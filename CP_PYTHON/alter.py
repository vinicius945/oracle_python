from bd import altera

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

mensagem_alterada = {
    'id': 1,  
    'assunto': 'por que você se foi?',
    'destinatario': 'vinicinreidelas@gmail.com',
    'remetente': 'vinicebo_gado@hotmail.com',
    'conteudo': 'Não me deixe, eu estou sofrendo. Mentira.'
}
altera(mensagem_alterada)

print("Mensagem alterada com sucesso.")
