# Usando o comando For ou While faça um algoritmo em Python que mostre qual índice
# cada letra pertence

string = input("Type any word: ")

for count in range(0, len(string)):
    print(f"The letter {string[count]} is in index {count}")