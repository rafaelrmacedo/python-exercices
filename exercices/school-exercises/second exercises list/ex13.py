# 13 – Utilizando o exercício anterior, também mostre a soma e a multiplicação dos seus
# dígitos separados.

number = "-1"
sum_number = int(0)
multiplication_number = int(1)

while int(number) < 0 or int(number) > 9999:
    number = input("Type a number between 0 and 9999: ")

for count in range(0, len(number)):
    sum_number += int(number[count])
    multiplication_number *= int(number[count])

print(f"Sum: {sum_number}")
print(f"Multiplication: {multiplication_number}")
