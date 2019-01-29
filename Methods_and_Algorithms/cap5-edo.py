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
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))

    return y


'''
def runge_kutta2(x0, y0, h, n):
    x = x0
    y = y0
    iterations = 0

    while iterations < n:
        y += h * f.f_derived(x)
        x += h
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))

    return y

def runge_kutta4(x0, y0, h, n):
    x = x0
    y = y0
    iterations = 0

    while iterations < n:
        y += h * f.f_derived(x)
        x += h
        print("I: " + str(iterations) +  "\tx: " + str(x) + "\ty: " + str(y))

    return y
'''