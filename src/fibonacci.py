# src/fibonacci.py

def fibonacci(n):
    if n < 0:
        raise ValueError("No se permiten números negativos")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
