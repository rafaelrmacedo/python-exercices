# 8 – Faça um programa em Python que receba 2 números inteiros e positivos e mostre todos
# os números primos entre estes 2 números

print("Program that calculates the prime number between 2 others prime numbers \n \n")

startNumber = "not a prime"
endNumber = "not a prime"

while startNumber == "not a prime" and endNumber == "not a prime":
    start = int(input("Type a prime number: "))

    if start > 1:
        for i in range(2, start):
            if start % i == 0:
                print(start, 'not a prime number')
                startNumber = "not a prime"
                break
        else:
            print(start, 'is a prime number')
            startNumber = "prime"
    elif start == 0:
        print(start, 'is zero. Zero is not a prime')
        startNumber = "not a prime"
    elif start == 1:
        print(start, 'is one. One is not a prime number')
        startNumber = "not a prime"
    else:
        print(start, 'is negative. Negative number is not a prime numbers')
        startNumber = "not a prime"

    end = int(input("Type another prime number: "))

    if end > 1:
        for i in range(2, end):
            if end % i == 0:
                print(end, 'not a prime number')
                endNumber = "not a prime"
                break
        else:
            print(end, 'is a prime number')
            endNumber = "prime"
    elif end == 0:
        print(end, 'is zero. Zero is not a prime')
        endNumber = "not a prime"
    elif end == 1:
        print(end, 'is one. One is not a prime number')
        endNumber = "not a prime"
    else:
        print(end, 'is negative. Negative number is not a prime numbers')
        endNumber = "not a prime"

for count in range(start + 1, end - 1):
    if count > 1:
        for x in range(2, count):
            if count % x == 0:
                break
        else:
            print(count)
