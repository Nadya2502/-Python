# сумма натуральных числе от 1 до n Равна формуле n(n+1)/2
def sum_natural_numbers(n:int):
    sum = 0

    for i in range (1, n+1):
        sum = sum + i

    sum2 = n*(n+1) / 2
    print(sum)
    print(sum2)

sum_natural_numbers(3)




