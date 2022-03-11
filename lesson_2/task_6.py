list_num = []

def function(num:int):
    num1 = num
    sum = 0
    while num !=0:
        sum = sum + num%10
        num = num//10
    return [num1, sum]

# Вводим список чисел пока не ввели EXIT
i = 0
while 1 == 1:
    a = input ('введите число ')
    if a == 'exit':
        break
    else:
        if a.isdigit():
            list_num.append(int(a))
            i = i + 1

# Формируем словарь число: сумма разрядов
list_result = {}
for lr in list_num:
    val1 = function(lr)
    list_result[val1[0]] = val1[1]


# Ищем максимальное значение
maxSum = 0
maxValue = 0
for key in list_result:
    if list_result[key] > maxSum:
        maxSum = list_result[key]
        maxValue = key


print(f'{maxValue} - {list_result[maxValue]}')





