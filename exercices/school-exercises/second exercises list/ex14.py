# 14 – Faça um programa que receba um número, sem especificar o tamanho, e mostre a soma
# de todos os seus dígitos.

number = ""
sum_number = int(0)

number = input("Type a number between 0 and 9999: ")

for count in range(0, len(number)):
    sum_number += int(number[count])

print(f"Sum: {sum_number}")
