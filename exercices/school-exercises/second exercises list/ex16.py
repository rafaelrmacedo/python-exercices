# 16 – Faça um programa que receba um número binário e faça a conversão dele para Decimal

decimal_number = int(0)
binary_number = input("Type a binary number: ")

if '0' in binary_number or '1' in binary_number:
    decimal_number = int(binary_number, base=2)
    print(f"Decimal number: {decimal_number}")
else:
    print("Type a binary number only!")
