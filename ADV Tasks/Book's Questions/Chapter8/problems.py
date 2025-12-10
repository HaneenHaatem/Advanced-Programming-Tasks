# ========================================================
# Problem 1: NumPy Operations

import numpy as np

arr = np.arange(1, 11)
mean = np.mean(arr)
median = np.median(arr)
standardDeviation = np.std(arr)

print("NumPy Operations:")
print(arr)
print(mean)
print(median)
print(standardDeviation)

# ========================================================
# Problem 2: Pandas Filtering

import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Omar', 'Zaid'],
    'Age': [20, 22, 19, 21],
    'Score': [85, 78, 92, 88]
}
df = pd.DataFrame(data)
high_scorers = df[df['Score'] > 80]
print("Students with Score > 80:")
print(high_scorers)

# ========================================================
# Problem 3: Visualization with Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure()
plt.plot(x, y, marker='o')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Numbers Line Graph')
plt.grid(True)
plt.show()

# ========================================================
# Problem 4: Flask Application
# Save this in a separate file, e.g., app.py

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, Advanced Python!"

if __name__ == '__main__':
    app.run(debug=True)

# ========================================================
# Problem 5: PyTorch Tensor Operations

import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

dot_product = torch.dot(tensor1, tensor2)
elementwise_mul = tensor1 * tensor2

print("PyTorch Operations:")
print(f"Tensor 1: {tensor1}")
print(f"Tensor 2: {tensor2}")
print(f"Dot Product: {dot_product}")
print(f"Element-wise Multiplication: {elementwise_mul}")

