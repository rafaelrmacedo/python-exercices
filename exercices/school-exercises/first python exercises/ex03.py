# 3 – Faça um programa que peça 5 números e imprima a média deles (Use FOR ou While)

averageNumber = 0
for count in range(5):
    number = int(input(f"Type the {count+1}° number: "))
    averageNumber = averageNumber + number

average = averageNumber / 5
print(f"The average value is {average}")