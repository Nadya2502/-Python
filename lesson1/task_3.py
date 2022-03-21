def line_equation(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    b = y1 - k*x1
    print (f'y = {k}*x+{b}')

line_equation(5, 4, 1, 2)