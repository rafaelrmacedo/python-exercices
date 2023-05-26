# 10 – Faça um programa que receba uma String e imprima ela com efeito em escada
# 11 – Repita o exercício anterior, mas agora ao contrário:

string = input("Type any word: ")

print("String pyramid:")
for count in range(0, len(string)):
    print(string[0: count + 1])

count = int(0)

print("Inverse string pyramid:")
for count in range(len(string), 0, - 1):
    print(string[0: count])
