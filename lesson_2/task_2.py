# вывод числа в обратном порядке
def reverse_number(n: int):
    b = 0
    while n != 0:

        b = b*10 + n%10
        n = n//10

    return b
print(reverse_number(2345))