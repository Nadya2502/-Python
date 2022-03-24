

def sum_three(a):
    sum = 0
    while (a != 0):
        sum = sum + a%10
        a = a//10

    return sum

print(sum_three(345))

def times_three(a):
    times = 1
    while (a != 0):
        times = times * (a%10)
        a = a//10
    return times

print(times_three(456))
