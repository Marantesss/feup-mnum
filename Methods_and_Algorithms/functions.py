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

### Exame 2018/19 ###

def f1(x, y):
    return math.sin(x + y) - math.exp(x - y)

def f2(x, y):
    return math.cos(x + y) - pow(x,2)*pow(y,2)

# derived f1 and f2

def f1_dx(x, y):
    return math.cos(y + x) - math.exp(x - y)

def f1_dy(x, y):
    return math.cos(x + y) + math.exp(x - y)

def f2_dx(x, y):
    return -math.sin(x + y) - 2 * pow(y, 2) * x

def f2_dy(x, y):
    return -math.sin(x + y) - 2 * pow(x, 2) * y