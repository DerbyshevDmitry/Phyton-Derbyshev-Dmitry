import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Применение декоратора timer к функции fibonacci без мемоизации
timed_fibonacci = timer(fibonacci)
print("Fibonacci without memoization:")
timed_fibonacci(300)

# Применение декоратора timer к функции fibonacci с мемоизацией
timed_memoized_fibonacci = timer(fibonacci)
print("\nFibonacci with memoization:")
timed_memoized_fibonacci(300)