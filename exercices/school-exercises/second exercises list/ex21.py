# 21 – Faça um programa que receba uma Frase e imprima quantas palavras a frase possui

phrase = input("Type a phrase: ")
words = int(0)
letter = ' '

words = [letter for letter in phrase if letter != ' ']

print(f"Quantity of words is: {words}")
