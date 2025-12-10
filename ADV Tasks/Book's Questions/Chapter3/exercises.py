#       Chapter 3 exercises:
# The first 8 questions about programming:

# ==================================================
# 1- remove_vowels(text) — Pure Function

def remove_vowels(text):
    return ''.join([char for char in text if char.lower() not in 'aeiou'])

print(remove_vowels("Hello World"))

# ==================================================
# 2- map + filter

numbers = [1, 2, 3, 4, 5, 6, 7]

result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, numbers)))

print(result)

# ==================================================
# 3- Recursive Fibonacci + lru_cache


from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

# ==================================================
# 4- Closure make_adder(n)

def make_adder(n):
    def add(x):
        return n + x
    return add

add5 = make_adder(5)
print(add5(10))   # 15

# ==================================================
# 5- apply_twice(func, value)

def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x + 1, 5)
print(result)  # 7

# ==================================================
# 6- Functional ETL Pipeline (tokenize → filter → count)

from functools import reduce
from collections import Counter

def etl_pipeline(texts):
    words = ' '.join(texts).lower().split()
    
    stopwords = {"the", "a", "is", "and", "on"}
    filtered = list(filter(lambda w: w not in stopwords, words))
    
    return dict(Counter(filtered))

texts = ["The cat is happy", "A cat and a dog"]
print(etl_pipeline(texts))  


# ==================================================
# 7- Implement your own reduce()
def my_reduce(func, iterable, initializer=None):
    iterator = iter(iterable)

    if initializer is None:
        value = next(iterator)
    else:
        value = initializer

    for item in iterator:
        value = func(value, item)

    return value
 
print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 10

# ==================================================
# 8- Decorator log_call(func)
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result
    return wrapper


@log_call
def say_hello():
    print("Hello!")

say_hello()