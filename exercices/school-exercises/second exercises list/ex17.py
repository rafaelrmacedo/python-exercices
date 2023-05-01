# 17 -Faça um programa que receba uma palavra e mostre se ela é um Palíndromo ou não:

string = input("Type any word: ")

if string[:: - 1] == string:
    print("The word is a palindrome.")
else:
    print("The word isn't a palindrome.")
    