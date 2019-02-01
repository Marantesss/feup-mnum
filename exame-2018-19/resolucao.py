import math

### Exercicio 2 ###

def f1(x, y):
    return math.sin(x + y) - math.exp(x - y)

def f2(x, y):
    return math.cos(x + y) - pow(x,2)*pow(y,2)

# derived f1 and f2

def f1_dx(x, y):
    return math.cos(y + x) - math.exp(x - y)

def f1_dy(x, y):
    return math.cos(x + y) + math.exp(x - y)

def f2_dx(x, y):
    return -math.sin(x + y) - 2 * pow(y, 2) * x

def f2_dy(x, y):
    return -math.sin(x + y) - 2 * pow(x, 2) * y

### Metodo de Newton ###

def metNewtonX(x, y):
    return x - (f1(x, y) * f2_dy(x, y) - f2(x, y) * f1_dy(x, y))/(f1_dx(x, y) * f2_dy(x, y) - f2_dx(x, y) * f1_dy(x, y))

def metNewtonY(x, y):
    return y - (f2(x, y) * f1_dx(x, y) - f1(x, y) * f2_dx(x, y))/(f1_dx(x, y) * f2_dy(x, y) - f2_dx(x, y) * f1_dy(x, y))

def ex2(x, y, n):
    iterations = 0
    xn = x
    yn = y
    print(xn, yn)
    while iterations < n:
        old_x = xn
        old_y = yn
        xn = metNewtonX(old_x, old_y)
        yn = metNewtonY(old_x, old_y)
        print(xn, yn)
        iterations += 1

ex2(-0.5, 1.0, 2)

### Exercicio 3 ###

A = [[10, 6, 1],
     [1, 11, 3],
     [2, 7, 13]]

b = [[2], [0], [-8]]

def ex3():
    x = y = z = 0.0
    for i in range(3):
        x = (b[0][0] - A[0][1]*y - A[0][2]*z)/A[0][0]
        y = (b[1][0] - A[1][0]*x - A[1][2]*z)/A[1][1]
        z = (b[2][0] - A[2][0]*x - A[2][1]*y)/A[2][2]
        print(i, x, y, z)

ex3()

### Exercicio 4 ###

def ex4():
    hx = hy = 1
    result = hx/2.0 * hy/2.0 * ((1.1 + 3 + 1.2 + 9.4) + 2*(2.1 + 1.5 + 2.2 + 1.4) + 4*4.5)
    print(result)

ex4()

### Exercicio 5 ###

def z_l(z, y):
    return -6 * z - 5 * y

def fy(z):
    return z

def ex5():
    x = 0
    h = 0.1
    y = 2
    z = 1
    for i in range(3):
        old_y = y
        old_z = z
        x += h
        y = old_y + h * fy(old_z)
        z = old_z + h * z_l(old_z, old_y)
        print(i, x, y, z)

ex5()