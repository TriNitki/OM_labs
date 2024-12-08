from methods import gradient_descent,  cauchy_method

def main():
    func = "x**3+y**3-15*x*y"
    print(gradient_descent(func, [5.23, 5.41]))
    print(cauchy_method(func, [5.23, 5.41]))

if __name__ == "__main__":
    main()