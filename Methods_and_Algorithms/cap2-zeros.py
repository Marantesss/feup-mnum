import functions as f

# pretendemos determinar o zero de function1, sabendo que se encontra no intervalo [0, 1]
# para terminar o ciclo iremos usar o criterio de precisao absoluta com valor 7e-6 ===> 7*10**-6
# -> abs(xn-1 - xn) > 7e-6
# ou seja, vamos parar as iteracoes quando o valor do intervalo for inferior ou igual a 7e-7

### Metodo da Bissecao ###

def metBissecao(a, b):
    iterations = 0
    while abs(a - b) > 7e-6:
        m = abs(a + b) / 2.0
        print(str(iterations) + ". M: " + str(m) + "\t a: " + str(a) + "\t b:" + str(b))
        if (f.function1(a) * f.function1(m)) < 0:
            b = m
        else:
            a = m
        iterations += 1

    print("Total de iteracoes: " + str(iterations))
    print("Melhor apoximacao: " + str(m))
    return (str(iterations), str(m))

### Metodo da Corda ###

def metCorda(a, b):
    iterations = 0
    zero = (a+b)/2
    old_a = a
    while abs(old_a - zero) > 7e-6:
        old_a = a
        zero = (a*f.function1(b) - b*f.function1(a)) / (f.function1(b) - f.function1(a))
        print(str(iterations) + ". M: " + str(zero) + "\t a: " + str(a) + "\t b:" + str(b))
        if (f.function1(a) * f.function1(zero)) < 0:
            b = zero
        else:
            a = zero
        iterations += 1

    print("Total de iteracoes: " + str(iterations))
    print("Melhor apoximacao: " + str(zero))
    return (str(iterations), str(zero))

### Metodo da Tangente ###

def metTangente(x):
    iterations = 0
    old_x = 0
    while abs(old_x - x) > 7e-6:
        old_x = x
        x = (x - f.function1(x)/f.derived_function1(x))
        print(str(iterations) + ". M: " + str(x))
        iterations += 1

    print("Total de iteracoes: " + str(iterations))
    print("Melhor apoximacao: " + str(x))
    return (str(iterations), str(x))


bissecao = metBissecao(0, 1)
corda = metCorda(0, 1)
tangente = metTangente(1)
print("-------------------")
print("BISSECAO - \tIteracoes: " + bissecao[0] + "\tAproximacao: " + bissecao[1])
print("CORDA - \tIteracoes: " + corda[0] + "\tAproximacao: " + corda[1])
print("TANGENTE - \tIteracoes: " + tangente[0] + "\tAproximacao: " + tangente[1])

'''OUTPUT:
BISSECAO -      Iteracoes: 18   Aproximacao: 0.8667640686035156
CORDA -         Iteracoes: 9    Aproximacao: 0.8667595970801818
TANGENTE -      Iteracoes: 4    Aproximacao: 0.8667603991750858
'''