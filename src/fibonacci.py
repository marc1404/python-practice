def main():
    print("Iterative:")
    print("n=0 ->", fibonacci_iterative(0))
    print("n=1 ->", fibonacci_iterative(1))
    print("n=6 ->", fibonacci_iterative(6))
    print()
    print("Recursive:")
    print("n=0 ->", fibonacci_recursive(0))
    print("n=1 ->", fibonacci_recursive(1))
    print("n=6 ->", fibonacci_recursive(6))


def fibonacci_iterative(n):
    fib = [0, 1]

    if n < 2:
        return fib[n]

    for i in range(n - 1):
        fib.append(fib[i] + fib[i + 1])

    return fib[n]


def fibonacci_recursive(n):
    if n < 2:
        return n

    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


main()
