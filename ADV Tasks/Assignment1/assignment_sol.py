# ============ Assignment 1 Solutions ===================
# Name : Haneen Hatem Abdelaal 
# Section : 1

# ====================== 1 ========================
# Transform and Clean Data (Product Names)

products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]
cleaned = list(map(lambda p: p.strip().title(), products))
print("1 :", cleaned)

# ====================== 2 ========================
# Convert Temperatures (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print("2 :", fahrenheit)

# ====================== 3 ========================
# Apply Multiple Transformations (Square then add 10)
nums = [1, 2, 3, 4, 5]
result = list(map(lambda n: (n*n) + 10, nums))
print("3 :", result)

# ====================== 4 ========================
# Extract First and Last Characters
words = ["python", "lambda", "programming", "map", "function"]
chars = list(map(lambda w: (w[0], w[-1]), words))
print("4 :", chars)

# ====================== 5 ========================
# Nested Map Transformation (Challenge) (increase marks by 5%)
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
updated = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print("5 :", updated)

# ====================== 6 ========================
# program that normalizes a list of numbers between 0 and 1
nums2 = [10, 20, 30, 40, 50]
mn = min(nums2)
mx = max(nums2)
normalized = list(map(lambda x: (x - mn) / (mx - mn), nums2))
print("6 :", normalized)

# ====================== 7 ========================
# extract the length of each word in every sentence
sentences = [
    "hello world",
    "python is awesome",
    "map and lambda"
]
lengths = list(map(lambda s: list(map(lambda w: len(w), s.split())), sentences))
print("7 :", lengths)
