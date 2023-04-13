# 5 – Faça um programa que receba um número e calcule o fatorial deste número.

factorial = int(1)
number = int(input("Type a number to give you a factorial of this number: "))

for count in range(1, number+1):    
    factorial *= count

print(factorial)
