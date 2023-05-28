# Escreva um programa que lê do usuário uma lista de nomes e que lê um nome 'n' de
# pesquisa. O programa deverá escrever na tela “Nome encontrado” se ‘n’ for encontrado na
# lista. Senão, deverá imprimir “Nome não encontrado”.

nameList = []
nameSearch = False
nameSearchInput = ''
choose = ''

while choose != 'N':
    nameInput = input("Type a name: ").capitalize()

    if nameInput.count(' ') >= 1:
        print("Only single names. Type again.")
        while nameInput.count(' ') >= 1: # Each time the user type a compound name,
            # the loop will be actived
            nameInput = input("Type a name: ")
    else:
        nameList.append(nameInput)

    choose = input("Do you want to add another name? (Y/N)\n").upper()

    while choose != 'Y' and choose != 'N':
        print("Invalid option.")
        choose = input("Do you want to add another name? (Y/N)\n").upper()

while True:
    nameSearchInput = input("Type a name to find in a name list: ").capitalize()

    if nameSearchInput.isalpha():
        print(f"Typed name: {nameSearchInput}\n")
        if nameSearchInput in nameList:
            print("Name found.")
        break
    else:
        print("Type only names. Type again.")
