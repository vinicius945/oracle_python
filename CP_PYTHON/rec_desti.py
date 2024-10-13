from bd import recupera_destinatario

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

mensagens = recupera_destinatario('Emma@gmail.com')
if mensagens:
    for mensagem in mensagens:
        print(mensagem)
else:
    print("Nenhuma mensagem encontrada para esse destinatário.")