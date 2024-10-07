def _f(func: str, value: float, symbol: str = "x") -> float:
    return eval(func.replace(symbol, str(value)))

def bisection_method(func: str, a: float, b: float, tol: float = 1e-5) -> float:
    while abs(b - a) > tol:
        midpoint = (a + b) / 2
        if _f(func, midpoint - tol) < _f(func, midpoint + tol):
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

def golden_section_search(func: str, a: float, b: float, tol: float = 1e-5) -> float: 
    golden_ratio = (1 + 5 ** 0.5) / 2

    while abs(b - a) > tol:
        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio

        if _f(func, c) < _f(func, d):
            b = d
        else:
            a = c

    return (a + b) / 2