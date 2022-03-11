ins_year = int(input('Введите год'))
def year_leap(ins_year):
    if ins_year%4 == 0:
        return f'этот год високосный'
    else:
        return f'этот год невисокосный'

print(year_leap(ins_year))
