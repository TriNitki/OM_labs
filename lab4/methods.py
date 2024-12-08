from math import sqrt
from sympy import diff

def _f(func: str, value1: float, value2: float, symbol1: str = "x", symbol2: str = "y") -> float:
    return eval(func.replace(symbol1, str(value1)).replace(symbol2, str(value2)))

def _d(func: str, var: str = "x"):
    return str(diff(func, var))

def _g(func):
    grad = [_d(func, "x"), _d(func, "y")]  # Частные производные
    return grad

def norm(vector):
    return sqrt(sum(v**2 for v in vector))

def vector_add(v1, v2, alpha=1.0):
    return [v1[i] + alpha * v2[i] for i in range(len(v1))]

def find_lambda(func, x, grad, lambda_min=0, lambda_max=1, tol=1e-4):
    while lambda_max - lambda_min > tol:
        mid1 = lambda_min + (lambda_max - lambda_min) / 3
        mid2 = lambda_max - (lambda_max - lambda_min) / 3
        f1 = _f(func, *vector_add(x, grad, alpha=-mid1))
        f2 = _f(func, *vector_add(x, grad, alpha=-mid2))
        if f1 < f2:
            lambda_max = mid2
        else:
            lambda_min = mid1
    return (lambda_min + lambda_max) / 2

def gradient_descent(func, x0, learning_rate=0.03, tol=1e-4, max_iter=1000):
    x = x0[:]
    num_iterations = 0

    for i in range(max_iter):
        grad = _g(func)
        grad_values = [_f(grad[0], *x), _f(grad[1], *x)]
        x_new = [x[i] - learning_rate * grad_values[i] for i in range(len(x))]

        if norm(grad_values) < tol:
            break

        x = x_new
        num_iterations += 1

    return x, i

# Метод Коши
def cauchy_method(func, x0, tol=1e-4, max_iter=100):
    x = x0[:]
    for i in range(max_iter):
        grad = _g(func)
        grad_values = [_f(grad[0], *x), _f(grad[1], *x)]
        
        if norm(grad_values) < tol:
            break
        
        _lambda = find_lambda(func, x, grad_values)
        
        x = vector_add(x, grad_values, alpha=-_lambda)
    
    return x, i