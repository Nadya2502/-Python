# Сколько раз встречается цифра в заданном числе
def find_number(n:int, n1:int):
    n = int(input('Введите цифру'))
    n1 = int(input('Введите число'))
    counter = 0
    while n1 != 0:
       if n1%10 == n :
           counter = counter + 1
       n1 = n1 // 10

    return f'эта цифра встречается {counter} раз'

print (find_number(5, 2453475678555))