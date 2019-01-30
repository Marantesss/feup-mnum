import functions as f

### Metodo de Euler ###
# Dado as condicoes iniciais (x0, y0) e a equando diferencial ordinario dy/dx = f(x,y)
# Escolhemos o passo de integracao h:
# a variavel independente parte de x0 e vai sofrendo sucessivos incrementosd de h:
# -> (xn+1 = xn + h)
# a variavel dependente y, obtem-se a partir de h e f(x, y):
# -> yn+1 = yn + h * f(xn, yn)

def euler(x0, y0, h, n):
    x = x0
    y = y0
    iterations = 0

    while iterations < n:
        y += h * f.f_derived(x)
        x += h
        iterations += 1
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))
    return y

s = euler(0, 0, 0.5, 40)
sl = euler(0, 0, 0.25, 80)
sll = euler(0, 0, 0.125, 160)
print("s: " + str(s) + "\tsl: " + str(sl) + "\tsll: " + str(sll))
print((sl - s)/(sll - sl))

### Metodo de Runge-Kutta 2 ###
# Dado a EDO dy/dx = f(x, y) e as condicoes iniciais (x0, y0) escolhe-se
# o passo de integracao h

def runge_kutta2(x0, y0, h, n):
    x = x0
    y = y0
    iterations = 0

    while iterations < n:
        d1 = h * f.function7(x, y)
        
        y += h * f.function7(x + h/2.0, y + d1/2.0)
        x += h
        iterations += 1
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))

    return y

s = runge_kutta2(0, 0, 0.1, 100)
sl = runge_kutta2(0, 0, 0.05, 200)
sll = runge_kutta2(0, 0, 0.025, 400)
print("s: " + str(s) + "\tsl: " + str(sl) + "\tsll: " + str(sll))
print((sl - s)/(sll - sl))

### Metodo de Runge-Kutta 4 ###

def runge_kutta4(x0, y0, h, n):
    x = x0
    y = y0
    iterations = 0

    while iterations < n:
        # calculando as variaveis auxiliares
        d1 = h * f.function7(x, y)
        d2 = h * f.function7(x + h/2.0, y + d1/2.0)
        d3 = h * f.function7(x + h/2.0, y + d2/2.0)
        d4 = h * f.function7(x + h, y + d3)

        y += d1/6.0 + d2/3.0 + d3/3.0 + d4/6.0
        x += h
        iterations += 1
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))

    return y

s = runge_kutta4(0, 0, 0.1, 100)
sl = runge_kutta4(0, 0, 0.05, 200)
sll = runge_kutta4(0, 0, 0.025, 400)
print("s: " + str(s) + "\tsl: " + str(sl) + "\tsll: " + str(sll))
print((sl - s)/(sll - sl))