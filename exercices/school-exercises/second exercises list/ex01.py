# 1 - crie uma variável string que receba a frase “MANIPULAÇÃO DE STRING”:
# a) Imprima a frase inteira
# b) Imprima somente a primeira Letra
# c) Imprima somente a última Letra
# d) Imprima somente a palavra “MANIPULAÇÃO”
# e) Imprima somente a palavra “DE”
# f) Imprima somente a palavra “STRING”
# g) Imprima somente as letras com os índices Impares
# h) Imprima somente as letras com os índices Pares
# i) Imprima a String de trás para frente

string = "MANIPULAÇÃO DE STRING "

# a)
print(f"Palavra inteira: {string}")

# b)
print(f"Primeira letra: {string[0]}")

# c)
print(f"Ultima letra: {string[20]}")

# d)
print(f"Palavra 1: {string[0: 11]}")

# e)
print(f"Palavra 2: {string[12: 14]}")

# f)
print(f"Palavra 3: {string[15: 21]}")

# g)
print("Letras aapenas com o índice impar: ")
for count in range(0, len(string)):
    if count % 2 != 0:
        print(string[count])

# h)
print("Letras aapenas com o índice par: ")
for count in range(0, len(string)):
    if count % 2 == 0:
        print(string[count])

# i)
print("Palavra ao contrário: ")
for count in range(len(string), 0):
    print(f"Palavra ao contrário: {count}")
