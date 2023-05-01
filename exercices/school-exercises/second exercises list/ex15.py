# 15 – Faça um programa que receba um número binário e verifique quantos números 0 e 1 tem
# esse número.

zeros = int(0)
ones = int(0)
binary_number = input("Type a binary number: ")

if '0' in binary_number or '1' in binary_number:
    for count in range(0, len(binary_number)):
        if binary_number[count] == '0':
            zeros += 1
        elif binary_number[count] == '1':
            ones += 1
    print(f"Quantity of zeros: {zeros}")
    print(f"Quantity of ones: {ones}")

else:
    print("Type a binary number only!")


