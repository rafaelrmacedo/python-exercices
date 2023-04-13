# 9 - Escreva um programa que replique o padrão de números a seguir, tal que o usuário
# insira o enésimo termo.
# 1. 1
# 2. 12
# 3. 123
# 4. 1234
# 5. 12345
# 6. 123456
# 7. 1234567
# 8. 12345678
# 9. 123456789
# 10. 12345678910
# 15. 12345678910...15

number = int(input("Type a number: "))

for count in range(1, number + 1):
    print(f"{count}° line: {count}")
