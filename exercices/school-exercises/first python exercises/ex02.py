# 2 – Faça um programa que receba um número inteiro e mostre sua tabuada do 0 ao 9.

multTableNumber = int(input("Type a number to do a multiplication table: \n"))

for count in range(10):
    print("%d x %d = %d" % (multTableNumber, count+1, multTableNumber*(count+1)))
