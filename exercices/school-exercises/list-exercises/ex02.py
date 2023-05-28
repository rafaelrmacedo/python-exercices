# Escreva um programa que lê do usuário uma lista de números e imprima a soma do primeiro
# e do último elemento da lista


def sumFirstLastNum(list):
    numberSum = list[0] + list[len(list) - 1]
    print(f"The sum is: {numberSum}")


list = []
choose = ''

while choose != 'N':
    numberInput = int(input("Type a number: "))
    list.append(numberInput)

    choose = input("Do you want to add another number? (Y/N) \n")
    choose = choose.upper()

    if choose != 'Y' and choose != 'N':
        print("Invalid option.")

print(sumFirstLastNum(list))