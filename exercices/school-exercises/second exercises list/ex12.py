# 12 – Faça um programa que receba um número de 0 até 9999 e mostre na tela cada um dos
# dígitos separados

number = "-1"

while int(number) < 0 or int(number) > 9999:
    number = input("Type a number between 0 and 9999: ")

for count in range(0, len(number)):
    print(f"Index {count} -> {number[count]}")

