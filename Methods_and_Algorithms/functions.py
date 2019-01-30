import math

def function1(x):
    return x**4 + 2*x**3 - x - 1

def derived_function1(x):
    return 4*x**3 + 6*x**2 - 1

def function2(x):
    return math.exp(x)

def function3(x):
    return math.cos(x)

def function5(x):
    return math.sin(x)

def function4(x):
    return x**4 - 2*x**3 - x - 1

def derived_function4(x):
    return 4*x**3 - 6*x**2 - 1

def function6(x, y):
    return x * y

def function7(x, y):
    return x + y

def function8(x):
    return pow(x + 1, 2) - 5

def f_derived(x):
	return pow(x, 3)

def f(x):
	return pow(x, 4)/4.0

def f_grad(x, y):
    return pow(x + 2, 2) + pow(y + 2, 2) - 5

def f_grad_dx(x, y):
    return 2 * (x + 2)

def f_grad_dy(x, y):
    return 2 * (y + 2)