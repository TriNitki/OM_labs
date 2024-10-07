from methods import nelder_mead, hooke_jeeves


def main():
    func = "x**3+y**3-15*x*y"
    initial_simplex = [[0, 0], [0.1, 0], [0, 1]]
    x_start = [5.23, 4.41]
    
    result1 = nelder_mead(func, initial_simplex)
    result2 = hooke_jeeves(func, x_start)
    
    print(result1, result2)
    
if __name__ == "__main__":
    main()