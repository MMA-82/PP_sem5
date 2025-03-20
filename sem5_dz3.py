"""
Создайте функцию генератор чисел Фибоначчи.
"""


def fibo():
    """
    генератор чисел Фибоначчи.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = fibo()
    for i in range(int(input("Сколько хотите увидеть чисел Фибоначчи?: "))):
        print(next(n))
