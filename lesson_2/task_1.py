
# количество четных и нечетных цифр в числе
def count_numbers(n: int):
    num_even = 0
    num_odd = 0

    while n != 0:
        if n%2 == 0:
            num_even = num_even + 1

        else:
            num_odd = num_odd +1
        n = n//10
    return f'в этом числе {num_even} четных чисел и {num_odd} нечетных'



print(count_numbers(23456))
