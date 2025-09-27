# fibonacci.py

def fibonacci_iterative(n: int) -> list[int]:
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

def fibonacci_recursive(n: int) -> int:
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = int(input("Введіть кількість чисел Фібоначчі: "))

    print("\nІтеративний метод:")
    print(fibonacci_iterative(n))

    print("\nРекурсивний метод (тільки n-те число):")
    print(f"{n}-те число Фібоначчі = {fibonacci_recursive(n-1)}")
