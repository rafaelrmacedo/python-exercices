# 1 - Crie uma agenda com 5 cadastros que possua nome (chave) e telefone (valor), após peça
# para digitar um nome e retorne se está no dicionário ou não.

contats  = {'Rafael': 982113046, 'Mae': 43987493, 'Pai': 42342342342,
            'Mae2': 89047623946, 'Pai2': 190846396}

userInput = input('Type a name: ').capitalize()

if userInput in contats:
    print('Exist in contats')
else:
    print("Doesn't exist in contats")