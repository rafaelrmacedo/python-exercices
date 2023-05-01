# 4 – Faça um programa que receba uma String e troque a letra do índice 4 e 5 pela letra “A”.
# Caso não exista esses índices deve retornar: “índices indisponíveis”. Use concatenação de
# Strings.

indexAvaliable = False

while indexAvaliable == False:
    string = input("Type any word: ")

    if len(string) < 4:
        print("Indexes unavailable.")
        indexAvaliable = False
    else:
        indexAvaliable = True
        string = string[0: 3] + "a" + string[4:5] + "a" + string[6: len(string)]


print(string)
