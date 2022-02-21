len1 = int(input('Введите длину первого отрезка:'))
len2 = int(input('Введите длину второго отрезка:'))
len3 = int(input('Введите длину третьего отрезка:'))
def exists_triangle (len1,len2,len3):
    if len1 + len2 <= len3 or len2 + len3 <= len1 or len1 + len3 <= len2:
        return f'такого треугольника не существует'

    return f'такой треугольник существует'


print(exists_triangle(len1, len2, len3))

def triangle(len1, len2, len3):
    if len1 + len2 <= len3 or len2 + len3 <= len1 or len1 + len3 <= len2:
        return None
    if len1 == len2 and len1 == len3:
        return f'такой треугольник равносторонний'
    if len1 == len2 or len2 == len3 or len1 == len3:
        return f'такой треугольник равносторонний'
    if len1 != len2 and len1 != len3:
        return f'такой треугольник разносторонний'

print(triangle(len1, len2, len3))
