# 7 – Faça um programa que receba uma String e mostre quantos espaços em branco ela possui
# Saída:

emptySpaces = int(0)
string = input("Type any word: ")

for count in range(0, len(string)):
    if string[count] == " ":
        emptySpaces += 1
        print(f"Empty spaces in string: {emptySpaces}")
