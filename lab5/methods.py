from sympy import diff
import math

def _f(func: str, value1: float, value2: float, symbol1: str = "x", symbol2: str = "y") -> float:
    return eval(func.replace(symbol1, str(value1)).replace(symbol2, str(value2)))

def _d(func: str, var: str = "x"):
    return str(diff(func, var))

def _g(func):
    grad = [_d(func, "x"), _d(func, "y")]
    return grad

def penalty_method(func, constraint_func, x_start, penalty_coef=100, learning_rate=0.01, tol=1e-5, max_iter=1000):
    x = x_start[:]
    num_iterations = 0
    
    while num_iterations < max_iter:
        constraint_val = _f(constraint_func, *x)
        penalty_term = penalty_coef * max(0, constraint_val)**2  # Штрафной член
        total_func_val = _f(func, *x) + penalty_term  # Функция с штрафом
        
        grad = _g(func)
        grad_values = [_f(grad[0], *x), _f(grad[1], *x)]
        
        x_new = [x[i] - learning_rate * grad_values[i] for i in range(len(x))]

        if all(abs(x_new[i] - x[i]) < tol for i in range(len(x))):
            break

        x = x_new
        num_iterations += 1

    return x, total_func_val