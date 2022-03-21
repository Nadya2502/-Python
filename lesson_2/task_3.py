def sum_numbers (n:int):
    a = 0
    b = 1
    for i in range (n):
        a = b +1
        b = b /-2
    return b

print(sum_numbers(4))