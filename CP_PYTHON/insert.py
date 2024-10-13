from bd import inclui

"""
Vinicius Prates Altafini RM559183
Enzo Dias Alfaia Mendes RM 558438
Enzo Prado Soddano RM 557937
"""

nomes = ['Emma', 'Eren', 'Carolindo', 'Romero', 'Leitica(Quebrou o meu coração)', 
         'Rafaela(Me deu vácuo)', 'Giovana', 'Igor', 'Eduardo', 'Julyana', 
         'Maria', 'Osvaldo', 'Pedro', 'Vinicius', 'Enzo', 'ENzo 2', 
         'Yuri Alberto', 'Cássio', 'xander', 'quentin']

dominios = ['gmail.com', 'hotmail.com', 'microsoft.com', 'tribu.com', 
            'fuu.com', 'drake.com', 'driven.com', 'Dark.com', 
            'space.com', 'meta.com']

mensagens = ['Olá!, queria dizer que estou melhorando', 'Ela partiuuuuuuuuuuu', 
             'Love of my lifeeeeeeeeeeee', 'You broken my hearth',
             'you leave-me', 'Mentirosa', 'Minecraft é demais', 
             'uau, que poracaria', 'Olá Professor!', 'Meu deus',
             'Me amava nada', 'me gusta', 'Um anel', 
             'três anéis para os elfos', 'Sauron', 'Melkor', 
             'Ainda estou triste pla minha gatinha', 
             'Ainda sinto falta da minha bellinha', 
             'A Bella me amou do começo ao fim', 
             'Eu poderia ter feito mais pela Bellinha e pelo Teddinho']


for i in range(20):
    nome_destinatario = nomes[i % len(nomes)]  
    dominio_destinatario = dominios[i % len(dominios)]  
    nome_remetente = nomes[(i + 1) % len(nomes)]  
    dominio_remetente = dominios[(i + 1) % len(dominios)]
    
    
    mensagem = mensagens[i % len(mensagens)] if i < len(mensagens) else 'Mensagem padrão'

    
    mensagem_dict = {
        'assunto': f'Assunto {i + 1}',  # Assunto incremental
        'destinatario': f'{nome_destinatario}@{dominio_destinatario}',
        'remetente': f'{nome_remetente}@{dominio_remetente}',
        'conteudo': mensagem
    }

    
    inclui(mensagem_dict)

print("20 Mensagens inseridas com sucesso.")
