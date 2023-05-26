# 22 – Faça um programa que receba uma String e troque todas as vogais por números: “A”
# troca pelo número 1, “E” pelo número 2 e assim sucessivamente.

input_string = input("Type any string: ")

new_string = input_string.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
for count in range(0, len(input_string)):
    if vowels[count] == input_string[count]:
        input_string[count] = vowels.index()

print(new_string)



