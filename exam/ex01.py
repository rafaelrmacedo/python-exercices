number = input("Type a number")
number_plus_one = ''
sum = 0

for digit in number:
    if digit == '9':
        digit.replace(digit, '0')

    sum = int(digit) + 1
    number_plus_one += str(sum)

print(number_plus_one)
