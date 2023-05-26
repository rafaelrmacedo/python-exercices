# 8 – Faça um programa que receba uma String e conte quantas vogais ela possui
# 9 – Faça um programa que receba uma String e conte quantas consoantes ela possui
string = input("Type any word: ")
consonant_quantity = int(0)
vowel_quantity = int(0)

string.lower()
for count in range(0, len(string)):
    if (
        (string[count] == "a")
        or (string[count] == "e")
        or (string[count] == "i")
        or (string[count] == "o")
        or (string[count] == "u")
    ): # posso fazer do jeito mais compacto, como vogais = "valores" e if string in vogais
        vowel_quantity += 1
    else:
        consonant_quantity += 1

print(f"Vowel quantity: {vowel_quantity}")
print(f"Consonant quantity: {consonant_quantity}")
