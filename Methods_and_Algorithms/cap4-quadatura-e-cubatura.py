import functions as f
import math

### Regra dos Trapezios ###
# A regra dos trapezios consiste em divir o intervalo de integracao [a, b]
# em n sub-intervalos igualmenet espacados de amplitude h (passo de integracao)

def trapezios(a, b, n):
    trapProcessados = 0
    area = 0
    h = float((b - a) / n)
    x = a

    while trapProcessados < n:
        area += (f.function5(x + h) + f.function5(x))/2.0 * h
        x += h
        trapProcessados += 1
    print(area)
    return area

### Regra de Simpson ###

def simpson(a, b, n):
    trapProcessados = 1
    area = 0
    h = float((b - a) / n)

    while trapProcessados < n - 1:
        if trapProcessados % 2 == 0:
            area += 2 * f.function5(a + trapProcessados * h)
        else:
            area += 4 * f.function5(a + trapProcessados * h)
        trapProcessados += 1
    
    area = (f.function5(a) + area + f.function5(b)) * (h / 3.0)
    print(area)
    return area

print("----- Trapezios -----")
print("n = 10")
I = trapezios(0, math.pi, 10)
print("n = 20")
I_l = trapezios(0, math.pi, 20)
print("n = 40")
I_ll = trapezios(0, math.pi, 40)
print("Q.C: " + str((I_l - I)/(I_ll - I_l)))

print("----- Simpson -----")
print("n = 10")
I = simpson(0, math.pi, 10)
print("n = 20")
I_l = simpson(0, math.pi, 20)
print("n = 40")
I_ll = simpson(0, math.pi, 40)
print("Q.C: " + str((I_l - I)/(I_ll - I_l)))

### Cubatura ###

# vamos usar a funcao6(x, y) = x * y;
# divindo em 4 partes (hx, hy)
# dominio de integracao x = [0, 2] e y = [0, 2]

def cubTrapezio(hx, hy, sum0, sum1, sum2,):
    return (hx*hy/4.0) * (sum0 + 2 * sum1 + 4 * sum2)

def cubSimpson(hx, hy, sum0, sum1, sum2,):
    return (hx*hy/9.0) * (sum0 + 4 * sum1 + 16 * sum2)

# calculando h's
hx = (2 - 0)/2.0
hy = (2 - 0)/2.0
# calculando somas
# sum0 representa os "vertices" dos limites de integracao
sum0 = f.function6(0,0) + f.function6(2,0) + f.function6(0,2) + f.function6(2,2)
# sum1 representa as "arestas" dos limites de integracai
sum1 = f.function6(0, hy) + f.function6(2, hy) + f.function6(hx ,0) + f.function6(hx, 2)
# sum2 representa o "centro" dos limites de integracao
sum2 = f.function6(hx, hy)

print("----- Trapezio -----")
print(cubTrapezio(hx, hy, sum0, sum1, sum2))

print("----- Simpson -----")
print(cubSimpson(hx, hy, sum0, sum1, sum2))
