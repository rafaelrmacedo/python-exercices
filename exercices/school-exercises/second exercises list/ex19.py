# 19 – Faça um programa que receba uma palavra ou frase e remova todos os acentos das
# letras,imprima a String sem acento.

import unicodedata

string = input("Type any word or phrase: ")
string = ''.join(letter for letter in unicodedata.normalize('NFD', string)
                 if not unicodedata.combining(letter))
print(string)
