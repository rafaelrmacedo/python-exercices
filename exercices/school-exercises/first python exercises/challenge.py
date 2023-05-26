number = input("Type a number in binary: \n")
numberInHexa = int(0)
value = int(2)

for count in range(0, len(number)):
    if number[count] == 1:
        numberInHexa += value ** count

print(numberInHexa)
