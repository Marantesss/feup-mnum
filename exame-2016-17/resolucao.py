import math

### Exercicio 2 ###

def f1(x, y):
    return math.pow(x, 2) - y - 1.2

def f2(x, y):
    return - x + math.pow(y, 2) - 1

def f1_dx(x, y):
    return 2 * x

def f1_dy(x, y):
    return - 1

def f2_dx(x, y):
    return - 1

def f2_dy(x, y):
    return 2 * y

### Metodo de Newton para resolver sistemas de equacoes lineares ###
def ex2(x0, y0):
    x = x0
    y = y0
    print(0, x, y)
    for i in range(2):
        old_x = x
        old_y = y
        x -= (f1(old_x, old_y)*f2_dy(old_x, old_y) - f2(old_x, old_y)*f1_dy(old_x, old_y)) / (f1_dx(old_x, old_y)*f2_dy(old_x, old_y) - f2_dx(old_x, old_y)*f1_dy(old_x, old_y))
        y -= (f1_dx(old_x, old_y)*f2(old_x, old_y) - f2_dx(old_x, old_y)*f1(old_x, old_y)) / (f1_dx(old_x, old_y)*f2_dy(old_x, old_y) - f2_dx(old_x, old_y)*f1_dy(old_x, old_y))
        print(i+1, x, y)

print("_____ Exercicio 2 _____")
ex2(1.0, 1.0)

### Exercicio 4 ###

def f4(x):
    return math.pow(x, 7) + 0.5*x - 0.5

### Metodo da corda ###
def ex4(e, d):
    a = e # extremo esquerdo
    b = d # extremo direito
    for i in range(4):
        x = (a*f4(b) - b*f4(a)) / (f4(b) - f4(a))
        print(i, a, b, x)
        if f4(x) < 0:
            a = x
        else:
            b = x

print("____ Exercicio 4 _____")
ex4(0.0, 0.8)


### Exercicio 5 ###

def f5(t, y, z):
    return 0.5 + math.pow(t, 2) + t * z

def z_dt(t, y, z):
    return 0.5 + math.pow(t, 2) + t * z

def z_(t, y, z):
    return z

def ex5(t0, y0, z0, h):
    print("__ Metodo de Euler __")
    t = t0
    y = y0
    z = z0
    print(0, t, y)
    for i in range(2):
        old_z = z
        z += h * z_dt(t, y, z)
        y += h * z_(t, y, old_z)
        t += h
        print(i+1, t, y)

    print("")
    print("__ Metodo de RK4 __")
    t = t0
    y = y0
    z = z0
    print(0, t, y)
    for i in range(2):
        old_z = z
        # d1
        dz1 = h * z_dt(t, y, z)
        dy1 = h * z_(t, y, old_z)
        # d2
        dz2 = h * z_dt(t + h/2.0,y + dy1/2.0, z + dz1/2.0)
        dy2 = h * z_(t + h/2.0, y + dy1/2.0, old_z + dz1/2.0)
        # d3
        dz3 = h * z_dt(t + h/2.0, y + dy2/2.0, z + dz2/2.0)
        dy3 = h * z_(t + h/2.0, y + dy2/2.0, old_z + dz2/2.0)
        # d4
        dz4 = h * z_dt(t + h, y + dy3, z + dz3)
        dy4 = h * z_(t + h, y + dy3, old_z + dz3)
        # valores a serio :)
        z += dz1/6.0 + dz2/3.0 + dz3/3.0 + dz4/6.0
        y += dy1/6.0 + dy2/3.0 + dy3/3.0 + dy4/6.0
        t += h
        print(i+1, t, y)

print("_____ Exercicio 5 _____")
ex5(0.0, 0.0, 1.0, 0.25)


### Exercicio 5 ###

def f6(x):
    return math.exp(1.5 * x)

def f6_dx(x):
    return 1.5 * math.exp(1.5 * x)

def L(x):
    return math.sqrt(1 + math.pow(f6_dx(x), 2))

def metTrap(a, b, h):
    area = L(a) + L(b)
    x = a + h
    while x != b:
        area += 2 * L(x)
        x += h
    area = h/2 * area
    print(area)
    return area

def metSimpson(a, b, h):
    area = L(a) + L(b)
    x = a + h
    i = 1
    while x != b:
        if i % 2 == 0:
            area += 2 * L(x)
        else:
            area += 4 * L(x)
        x += h
        i += 1
    area = h/3 * area
    print(area)
    return area

def ex6():
    print("__ Metodo dos Trapezios __")
    T = metTrap(0, 2, 0.5)
    T_l = metTrap(0, 2, 0.25)
    T_ll = metTrap(0, 2, 0.125)
    print("Q.C: " + str((T_l - T)/(T_ll - T_l)))
    print("Erro: " + str((T_ll - T_l)/3.0))

    print("__ Metodo de Simpson __")
    S = metSimpson(0, 2, 0.5)
    S_l = metSimpson(0, 2, 0.25)
    S_ll = metSimpson(0, 2, 0.125)
    print("Q.C: " + str((S_l - S)/(S_ll - S_l)))
    print("Erro: " + str((S_ll - S_l)/15.0))

print("_____ Exercicio 6 _____")
ex6()
