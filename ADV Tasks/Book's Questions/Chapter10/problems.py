
# ========================================================
# Problem 1: Context Manager: Timer:

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        print(f"Execution took {self.elapsed} seconds")

with Timer():
    for i in range(1000000):
        pass


# ========================================================
# Problem 2: Generator: even_numbers:

def even_numbers(n):
    """Generator that yields even numbers up to n"""
    for i in range(2, n + 1, 2):
        yield i

def even_numbers_alt(n):
    """Alternative implementation using comprehension logic"""
    for num in range(1, n + 1):
        if num % 2 == 0:
            yield num

print("Testing even_numbers generator:")
for num in even_numbers(10):
    print(num)


# ========================================================
# Problem 3: Coroutine: filter_positive:

def filter_positive():
    while True:
        num = (yield)
        if num > 0:
            print(f"Positive number: {num}")

co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)


# ========================================================
# Problem 4: Factory Pattern: Shapes :

class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError(f"Unknown shape: {shape_type}")

shape = shape_factory("circle")
print(shape.draw())
# ========================================================
# Problem 5: Observer Pattern :
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received update: {message}")

subject = Subject()
obs1 = Observer()
obs2 = Observer()

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Update available!")