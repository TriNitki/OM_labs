from sympy import diff

def _f(func: str, value: float, symbol: str = "x") -> float:
    return eval(func.replace(symbol, str(value)))

def _d(func: str):
    return str(diff(func))


def newton_raphson_method(func, x0, tol=1e-4, max_iter=100):
    x = x0
    for _ in range(max_iter):
        f_prime = _f(_d(func), x)
        f_double_prime = _f(_d(_d(func)), x)
        if abs(f_prime) < tol:
            break
        x = x - f_prime / f_double_prime
    return x

def midpoint_method(func, a, b, tol=1e-4):
    while abs(b - a) > tol:
        midpoint = (a + b) / 2
        if _f(_d(func), midpoint) > 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2