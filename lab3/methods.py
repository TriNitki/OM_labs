def _f(func: str, value1: float, value2: float, symbol1: str = "x", symbol2: str = "y") -> float:
    return eval(func.replace(symbol1, str(value1)).replace(symbol2, str(value2)))

def simplex_method(func, initial_simplex, tol=1e-4, max_iter=1000):
    rho = 0.5
    sigma = 0.5
    
    simplex = initial_simplex[:]
    num_iterations = 0
    
    while num_iterations < max_iter:
        simplex.sort(key=lambda x: _f(func, *x))
        best = simplex[0]
        worst = simplex[-1]
        second_worst = simplex[-2]
        
        # Нахождение центра тяжести
        centroid = [(simplex[0][i] + simplex[1][i]) / 2 for i in range(2)]
        
        # Проецирование худшей вершины через центр тяжести
        reflection = [2 * centroid[i] - worst[i] for i in range(2)]
        if _f(func, *reflection) < _f(func, *best):
            simplex[-1] = reflection
        else:
            if _f(func, *reflection) < _f(func, *second_worst):
                simplex[-1] = reflection
            else:
                contraction = [centroid[i] + rho * (worst[i] - centroid[i]) for i in range(2)]
                if _f(func, *contraction) < _f(func, *worst):
                    simplex[-1] = contraction
                else:
                    simplex = [[best[i] + sigma * (x[i] - best[i]) for i in range(2)] for x in simplex]
        
        num_iterations += 1
        if max([abs(_f(func, *simplex[0]) - _f(func, *point)) for point in simplex[1:]]) < tol:
            break
    
    return simplex[0]

def hooke_jeeves(func, x0, step_size=0.5, step_reduction=0.5, tolerance=1e-4, max_iter=100):
    def explore(base_point, step_size):
        new_point = base_point[:]
        for i in range(len(base_point)):
            for direction in [-1, 1]:
                new_point[i] = base_point[i] + direction * step_size
                if _f(func, new_point[0], new_point[1]) < _f(func, base_point[0], base_point[1]):
                    base_point[i] = new_point[i]
                    break
                else:
                    new_point[i] = base_point[i]
        return base_point

    x_base = x0[:]  # Лучшая точка
    x_new = x0[:]   # Точка передвижения
    iteration = 0

    while step_size > tolerance and iteration < max_iter:
        x_new = explore(x_base, step_size)

        if _f(func, x_new[0], x_new[1]) < _f(func, x_base[0], x_base[1]):
            x_base = [2 * x_new[i] - x_base[i] for i in range(len(x_base))]
        else:
            step_size *= step_reduction

        iteration += 1

    return x_base