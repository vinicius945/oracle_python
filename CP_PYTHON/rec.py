from banco import recupera

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

mensagem = recupera(154) 
if mensagem:
    print(f"Mensagem recuperada: {mensagem}")
else:
    print("Mensagem não encontrada.")