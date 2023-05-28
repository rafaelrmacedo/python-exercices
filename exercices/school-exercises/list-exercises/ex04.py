# Escreva um programa que lê do usuário uma lista de números e imprima apenas os números
# negativos que são divisíveis por 3.

numberList = []
filteredNumberList = []
choose = ''

def printNegativeAndDivisibleBy3(numberlist):
    for count in range(0, len(numberlist)):
        if numberlist[count] % 3 == 0 and numberlist[count] < 0:
            filteredNumberList.append(numberlist[count])

    print("Filtered numbers: ")
    for count in filteredNumberList:
        print(count)

while choose != 'N':
    try:
        numberInput = int(input("Type a number: "))
        numberList.append(numberInput)
    except ValueError:
        print("Invalid number. Please enter only integer numbers.")
        continue

    choose = input("Do you want to add another number? (Y/N) \n").upper()

    while choose != 'Y' and choose != 'N':
        print("Invalid option.")
        choose = input("Do you want to add another name? (Y/N)\n").upper()

printNegativeAndDivisibleBy3(numberList)