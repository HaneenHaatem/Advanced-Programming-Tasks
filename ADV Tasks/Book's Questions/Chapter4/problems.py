# ========================================================
# Problem 1: Validate Email Addresses

import re

pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9-]+\.(com|org|edu)$'
emails = ["user@example.com", "bad-email", "test@domain.org"]

for e in emails:
    if re.match(pattern, e):
        print(e, "is valid email")
    else:
        print(e, "is not valid email")
# ========================================================
# Problem 2: Extract Hashtags

import re

text = "I love #Python and #AI"
tags = re.findall(r'#\w+', text)
print(tags)

# ========================================================
# Problem 3: Validate Phone Numbers

import re

pattern = r'^(\+1-)?\d{3}-\d{3}-\d{4}$'
numbers = ["+1-555-1234", "123-456-7890", "5551234"]
for t in numbers:
    if re.match(pattern,t):
        print(t, "is valid number")
    else:
        print(t, "is not valid number")

# ========================================================
# Problem 4: Word Frequency (Regex Tokenizer)

import re
from collections import Counter

text = "Python, Python! AI is great; Python AI."
words = re.findall(r'\b\w+\b', text.lower())  
freq = Counter(words)
print(freq)



# ========================================================
# Problem 5: Find Duplicate Words

import re

text = "This is is a test test"
duplicates = re.findall(r'\b(\w+)\s+\1\b', text)
print(duplicates)

# ========================================================
# Problem 6: Extract Dates

import re

text = "The events are on 2023-05-12 and 2024-01-01."
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(dates)


# ========================================================
# Problem 7: Mask Sensitive Data

import re

text = "Card: 1234-5678-9012-3456"
masked = re.sub(r'\d', '*', text[:-4]) + text[-4:]
print(masked)


# ========================================================
# Problem 8: Extract Programming Languages

import re

text = "I know Python, Java, and C++ but not Ruby."
languages = ['Python', 'Java', 'C++', 'Ruby']
result = [lang for lang in languages if lang in text]
print(result)