# 20 – Faça um programa que receba uma String no formato “DD/MM/AAAA” verifique se as
# barras estão no lugar certo, e imprima a Data por extenso: exemplo 15 de Maio de 2022

def valid_date(date_string):
    try:
        # faz o split e transforma em números
        day, mouth, year = map(int, date_string.split('/'))

        # mes ou ano inválido, retorna False
        if mouth < 1 or mouth > 12 or year <= 0:
            return False

        # verifica qual o último dia do mês
        if mouth in (1, 3, 5, 7, 8, 10, 12):
            last_day = 31
        elif mouth == 2:
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                last_day = 29
            else:
                last_day = 28
        else:
            last_day = 30

        # verifica se o dia é válido
        if day < 1 or day > last_day:
            return False

        for count in range(0, len(month_array)):
            if mouth == count + 1:
                mouth_string = month_array[count]

        print(f"Day {day} of {mouth_string} of {year}.")
        return True
    except ValueError:
        return False


date = ''
month_array = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

while not valid_date(date):
    date = input("Type any date (Use format dd/MM/yyyy): ")
    valid_date(date)
