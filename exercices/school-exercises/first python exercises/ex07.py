# 7 – Faça um programa em Python que receba um número inteiro e positivo e mostre se ele é
# primo ou não.

number = int(input("Type a number and you know if it's prime or not: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number")
            break
        else:
            print("It's prime number")
elif number == 0:
    print("It's zero. Not a prime number")
elif number == 1:
    print("It's one. Not a prime number")
else:
    print("It's negative. Not a prime number")
