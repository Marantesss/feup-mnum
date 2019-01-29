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

def f_derived(x):
	return pow(x, 3)

def f(x):
	return pow(x, 4)/4.0