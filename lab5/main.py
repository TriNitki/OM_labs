from methods import penalty_method, quadratic_penalty_method

def main():
    func = "(x - 6)**2 + (y - 6)**2"
    constraint_func = "x+y-8"
    print(penalty_method(func, constraint_func, [0, 0]))
    print(quadratic_penalty_method(func, 0, 0))

if __name__ == "__main__":
    main()