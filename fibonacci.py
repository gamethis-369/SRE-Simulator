def fibonacci_convergence(terms=50):
    fib = [0, 1]
    for i in range(2, terms + 1):
        fib.append(fib[i-1] + fib[i-2])
    ratios = [fib[i+1] / fib[i] for i in range(1, terms)]
    return ratios
