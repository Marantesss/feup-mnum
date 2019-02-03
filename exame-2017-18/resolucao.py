import math
### Exercicio 1 ###

def f1(x):
    return math.pow(x - 7, 2) + math.pow(x, 4)

B = (math.sqrt(5) - 1)/2.0
A = math.pow(B, 2)

def ex1():
    # metodo da seccao aurea
    x1 = 0
    x2 = 3
    x3 = x1 + A * (x2 - x1)
    x4 = x1 + B * (x2 - x1)
    print(x1, x3, x4, x2)
    while abs(x2 - x1) > 0.001:
        if f1(x3) < f1(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A * (x2 - x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B * (x2 - x1)
        print(x1, x3, x4, x2)
    
    # metodo da interpolacao quadrica
    a = x1
    b = x2
    m = (a + b) / 2.0
    h = (b - a) / 2.0
    minimo = m + (h * (f1(a) - f1(b))) / (2 * (f1(b) - 2 * f1(m) + f1(a)))
    print(minimo)

print("_____ EXERICIO 1 _____")
ex1()

### Exercicio 2 ###

def f2(x):
    return math.sqrt(1 + math.pow(2.5 * math.exp(2.5 * x), 2))

def ex2():
    a = 0
    b = 1
    h = 0.125
    ### metodo dos trapezios ###
    print("__ TRAPEZIOS __")
    # h = 0.125
    x = a + h
    area1 = f2(a) + f2(b)
    while x != b:
        area1 += 2 * f2(x)
        x += h
    area1 = (h/2.0) * area1 
    print(area1)
    # h = 0.0625
    h_l = h/2.0
    x = a + h_l
    area2 = f2(a) + f2(b)
    while x != b:
        area2 += 2 * f2(x)
        x += h_l
    area2 = (h_l/2.0) * area2 
    print(area2)
    # h = 0.03125
    h_ll = h/4.0
    x = a + h_ll
    area3 = f2(a) + f2(b)
    while x != b:
        area3 += 2 * f2(x)
        x += h_ll
    area3 = (h_ll/2.0) * area3 
    print(area3)
    # Q.C
    print((area2 - area1)/(area3 - area2))
    # Erro_ll
    print((area3 - area2)/3.0)

    ### metodo de simpson ###
    print("__ SIMPSON __")
    # h = 0.125
    x = a + h
    area1 = f2(a) + f2(b)
    i = 1
    while x != b:
        if i % 2 == 0:
            area1 += 2 * f2(x)
        else:
            area1 += 4 * f2(x)
        x += h
        i += 1
    area1 = (h/3.0) * area1 
    print(area1)
    # h = 0.0625
    h_l = h/2.0
    x = a + h_l
    area2 = f2(a) + f2(b)
    i = 1
    while x != b:
        if i % 2 == 0:
            area2 += 2 * f2(x)
        else:
            area2 += 4 * f2(x)
        x += h_l
        i += 1
    area2 = (h_l/3.0) * area2
    print(area2)
    # h = 0.03125
    h_ll = h/4.0
    x = a + h_ll
    area3 = f2(a) + f2(b)
    i = 1
    while x != b:
        if i % 2 == 0:
            area3 += 2 * f2(x)
        else:
            area3 += 4 * f2(x)
        x += h_ll
        i += 1
    area3 = (h_ll/3.0) * area3
    print(area3)
    # Q.C
    print((area2 - area1)/(area3 - area2))
    # Erro_ll
    print((area3 - area2)/15.0)

print("_____ EXERICIO 2 _____")
ex2()

### Exercicio 3 ###

# atrazves do programa plor2d() do maxima, vemos que f3(x) tem 2 zeros em [-6,-4] e [1,3]
def f3(x):
    return math.exp(x) - x - 5

def f3_dx(x):
    return math.exp(x) - 1

# converge no intervalo [-6,-4], ou seja, |f3_1(x)'| < 1 nesse intervalo
def f3_1(x):
    return math.exp(x) - 5

# converge no intervalo [1,3], ou seja, |f3_2(x)'| < 1 nesse intervalo
def f3_2(x):
    return math.log(5 + x)

def ex3():
    ### Picard-Peano ###
    print("Metodo de Picard-Peano")
    guess = 3
    for i in range(10):
        guess = f3_2(guess)
        print("I: " + str(i + 1) + "\tx: " + str(guess))

    print("")

    ### Metodo de Newton ###
    print("Metodo de Newton")
    x = 3
    for i in range(10):
        x -= f3(x) / f3_dx(x)
        print("I: " + str(i + 1) + "\tx: " + str(x))
    
ex3()

### Exericico 4 ###

#def ex4():