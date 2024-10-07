from methods import bisection_method, golden_section_search

def main():
    func = "x**4-10*x**3+36*x**2+5*x"
    a = 3
    b = 5
    result1 = bisection_method(func, a, b)
    result2 = golden_section_search(func, a, b)
    
    print(result1, result2)

if __name__ == "__main__":
    main()