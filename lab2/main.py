from methods import newton_raphson_method, midpoint_method


def main():
    func = "1/4*x**4+x**2-8*x+12"
    a = 0
    b = 2
    
    result1 = newton_raphson_method(func, 1)
    result2 = midpoint_method(func, a, b)
    
    print(result1, result2)
    
if __name__ == "__main__":
    main()