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
    
print("_____ EXERICIO 3 _____")
ex3()

### Exericico 4 ###

def dC_dt(C, T):
    return -math.exp(-0.5/(T + 273)) * C

def dT_dt(C, T):
    return 30 * math.exp(-0.5/(T + 273)) * C - 0.5 * (T - 20)

def euler(t, C, T, h, n):
    i = 0
    print(i, t, C, T)
    while i < n:
        t += h
        old_C = C
        old_T = T
        C += h * dC_dt(old_C, old_T)
        T += h * dT_dt(old_C, old_T)
        print(i + 1, t, C, T)
        i += 1

    return T
    
def rk4(t, C, T, h):
    i = 0
    print(i, t, C, T)
    for i in range(2):
        t += h
        old_C = C
        old_T = T
        # dy1
        dy1_C = h * dC_dt(old_C, old_T)
        dy1_T = h * dT_dt(old_C, old_T)
        # dy2
        dy2_C = h * dC_dt(old_C + dy1_C/2.0, old_T + h/2.0)
        dy2_T = h * dT_dt(old_C + h/2.0, old_T + dy1_T/2.0)
        # dy3
        dy3_C = h * dC_dt(old_C + dy2_C/2.0, old_T + h/2.0)
        dy3_T = h * dT_dt(old_C + h/2.0, old_T + dy2_T/2.0)
        # dy4
        dy4_C = h * dC_dt(old_C + dy3_C, old_T + h)
        dy4_T = h * dT_dt(old_C + h, old_T + dy3_T)
        # T e C
        C += (1.0/6.0) * (dy1_C + 2*dy2_C + 2*dy3_C + dy4_C)
        T += (1.0/6.0) * (dy1_T + 2*dy2_T + 2*dy3_T + dy4_T)
        print(i + 1, t, C, T)
    

def ex4():
    ### Metodo de Euler ###
    print("__ Metodo de Euler __")
    euler(0, 2.5, 25, 0.25, 3)

    ### Metodo de RK4 ###
    print("__ Metodo de RK4 __")
    rk4(0, 2.5, 25, 0.25)
    
    h = 0.25
    h_l = h/2.0
    h_ll = h/4.0
    T = euler(0, 2.5, 25, h, 2)
    T_l = euler(0, 2.5, 25, h_l, 4)
    T_ll = euler(0, 2.5, 25, h_ll, 8)
    print("__ ERROS __")
    print(T, T_l, T_ll)
    print("Q.C: " + str((T_l - T)/(T_ll - T_l)))
    print("Erro estimado: " + str((T_ll - T_l)/1.0)) # O metodo de Euler e de primeira ordem

    

print("_____ EXERICIO 4 _____")
ex4()