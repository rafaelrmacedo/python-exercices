# 4 – Faça um programa em python que receba do usuário 10 números aleatórios inteiros. Ao
# final do programa deve aparecer uma mensagem indicando qual maior e menor número
# digitado.

biggerNumber = int(0)
minorNumber = int(10)
number = int(0)

for count in range(10):
    number = int(input("Type a number: "))

    if number > biggerNumber:
        biggerNumber = number
    elif number < minorNumber:
        minorNumber = number

print(f"The bigger number is {biggerNumber} and the minor is {minorNumber}")
