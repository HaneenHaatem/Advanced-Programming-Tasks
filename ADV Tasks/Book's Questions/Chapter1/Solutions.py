# ================= 1 ======================
import this

# three principles that resonate most with my coding philosophy 
'''
1. Beautiful is better than ugly.
2. Simple is better than complex.
3. Now is better than never.
'''

# ================= 2 ======================
import dis

def square(x):
    return x * x

def multiply(a, b):
    return a * b

print("square function bytecode: ")
dis.dis(square)

print("multiply function bytecode: ")
dis.dis(multiply)

# ================= 3 ======================
data = 10
print("Type of integer:",type(data))

data = [1, 2, 3]
print("Type of list:",type(data))

def my_func():
    pass

data = my_func
print("Type of function:",type(data))

# ================= 4 ======================
# PyPy vs CPython:
# PyPy uses a JIT (Just-in-Time) compiler that dynamically compiles frequently executed Python code into machine code, offering significant speed improvements (often 5-10x faster) for long-running applications. It's ideal for CPU-intensive tasks like scientific computing or web servers.

# Jython vs CPython:
# Jython runs on the JVM (Java Virtual Machine), allowing Python code to interact seamlessly with Java libraries. It's perfect for integrating Python into existing Java ecosystems or leveraging JVM features like garbage collection and threading.

# Use cases:

# PyPy: Web servers, data processing pipelines, scientific simulations

# Jython: Enterprise applications needing Java libraries, Android development with Python

# ================= 5 ======================
import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)

print("AST dump:")
print(ast.dump(tree, indent=4))

# ================= 6 ======================
my_list = [10, 20, 30]

print("memory address:",id(my_list))

my_list.append(40)
print("memory address:",id(my_list))

print("Has the same value")
# The 2 memories have the same address
