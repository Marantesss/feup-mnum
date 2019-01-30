import functions as f
import math as m

### Pesquisa unidimensional ###

# 1. Enquadrar o minimo num intervalo [x1, x2]
# 2. Dterminar 2 pontos x3 e x4 dentro do intervalo [x1, x2]
# 3. Iteracao abaondona-se um dos extremos x1 ou x2
#   3.1 se f(x3) < f(x4) entao min esta no intervalo [x1, x4] e entao x1 = x1 e x2 = x4
#   3.2 se f(x3) > f(x4) entao min esta no intervalo [x3, x2] e entao x1 = x3 e x2 = x2

### Metodo dos tercos ###

def metTercos(a, b, final_interval):
    x1 = a
    x2 = b
    iterations = 0
    while x2 - x1 > final_interval:
        iterations += 1
        # calcular os pontos intermedios no intervalo [x1, x2]
        h = (x2 - x1)/ 3.0
        x3 = x1 + h
        x4 = x1 + 2 * h

        # calcular os novos extremos do intervalo
        if f.function8(x3) < f.function8(x4):
            x2 = x4
        else:
            x1 = x3

        print(iterations)


    print("x1: " + str(x1) + "\tx2: " + str(x2))
    return (x1, x2)

### Regra Aurea ###

def seccaoAurea(a, b, final_interval):
    iterations = 0
    B = (m.sqrt(5) - 1)/2.0
    A = B**2
    x1 = a
    x2 = b
    x3 = x1 + A*(x2 - x1)
    x4 = x1 + B*(x2 - x1)
    while x2 - x1 > final_interval:
        iterations += 1
        # calcular os novos extremos do intervalo
        if f.function8(x3) < f.function8(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A * (x2 - x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B * (x2 - x1)
        print(iterations)

    print("x1: " + str(x1) + "\tx2: " + str(x2))
    return (x1, x2)

### Interpolcao Quadratica ###
# Parte de 3 pontos x1, x2, x3 e ajusta uma parabola
# h = (b - a) / 2.0
# m = (a + b) / 2.0
# cujo minimo se encontra no ponto:
# x_min = x2 + h * (f(x1) - f(x3))/(2 * (f(x3) - 2 * f(x2) + f(x1))) 

def interpolacaoQuadratica(a, b):
    m = (a + b) / 2.0
    h = (b - a) / 2.0

    f1 = f.function8(a)
    f2 = f.function8(m)
    f3 = f.function8(b)

    return m + (h * (f1 - f3))/(2 * (f3 - 2 * f2 + f1))

interval = metTercos(-1000, 1000, 0.01) # minimo de f(x) = (x + 1)^2 + 5 e -1
print("Interpolacao Quadratica: " + str(interpolacaoQuadratica(interval[0], interval[1])))

''' Output -> 31 iteracoes
x1: -1.00362460447      x2: -0.996671144405
Interpolacao Quadratica: -1.0
'''

interval = seccaoAurea(-1000, 1000, 0.01) # minimo de f(x) = (x + 1)^2 + 5 e -1
print("Interpolacao Quadratica: " + str(interpolacaoQuadratica(interval[0], interval[1])))

'''Output -> 26 iteracoes
x1: -1.00493331065      x2: -0.997565281265
Interpolacao Quadratica: -1.0
'''

### Metodo do Gradiente ###
# Metodo autocorretor

def metGradiente(x0, y0, h0, num_iter):
    x = x0
    y = y0
    h = h0
    iterations = 0

    while iterations < num_iter:
        # calcular novos valores
        xn = x - h * f.f_grad_dx(x, y)
        yn = y - h * f.f_grad_dy(x, y)

        # tomar decisoes
        # se o valor da funcao diminui, duplicar o step e fazer nova iteracao
        if f.f_grad(xn, yn) < f.f_grad(x, y):
            x = xn
            y = yn
            h = 2 * h
        # se o valor da funcao aumentou, dividir o step para metade e fazer novamente a iteracao
        else:
            h = h/2

        iterations += 1
        print("I: " + str(iterations) + "\tx: " + str(x) + "\ty:" + str(y))
    
metGradiente(31415.92, -5028.45, 0.1, 100)

'''Output
...
I: 98   x: -1.99999993228       y:-2.00000001083
I: 99   x: -1.99999993228       y:-2.00000001083
I: 100  x: -2.00000004063       y:-1.9999999935
'''
