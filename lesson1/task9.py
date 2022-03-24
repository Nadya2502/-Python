num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
num3 = int(input('Введите третье число:'))
def middle_number(num1, num2, num3):
    if (num1 < num2 and num1 > num3) or (num1 < num3 and num1 > num2):
        return f'{num1} среднее число'
    if (num2 < num1 and num2 > num3) or (num2 < num3 and num2 > num1):
        return f'{num2} среднее число'
    if (num3 < num1 and num3 > num2) or (num3 < num2 and num3 > num1):
        return f'{num3} среднее число'
    else:
        return f'Введите разные числа'


print(middle_number(num1,num2, num3))