from bd import recupera

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

mensagem = recupera(77) 
if mensagem:
    print(f"Mensagem recuperada: {mensagem}")
else:
    print("Mensagem não encontrada.")