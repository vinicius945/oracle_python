from bd import recupera_assunto

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

mensagens = recupera_assunto('Assunto 20')
if mensagens:
    for mensagem in mensagens:
        print(mensagem)
else:
    print("Nenhuma mensagem encontrada com esse assunto.")