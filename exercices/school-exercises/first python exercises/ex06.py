# 6 - Considere um número inteiro positivo n especificado pelo usuário. Elabore um programa
# que calcule e mostre na tela:
# - A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;
# - A soma dos n primeiros números pares;
# - A soma dos n primeiros números ímpares.

firstNumbersNotNull = int(0)
number = int(input("Type a number: "))

for count in range(1, number + 1):
    firstNumbersNotNull = int(count + count)
    if count % 2 == 0:
        firstNumbersEven = int(count + count)

print(firstNumbersNotNull, firstNumbersEven)
