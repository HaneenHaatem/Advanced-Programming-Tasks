# ========================================================
# Problem 1: (CSV handling):

import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    print("Students with grade > 80:")
    for row in reader:
        if int(row['Grade']) > 80:
            print(row['Name'])

# ========================================================
# Problem 2: (JSON handling):
import json

data = {
    "course": "Python",
    "duration": "3 months",
    "students": ["Ali", "Sara"]
}

with open('course.json', 'w') as file:
    json.dump(data, file, indent=2)

with open('course.json', 'r') as file:
    loaded_data = json.load(file)
    print("Students:", loaded_data['students'])

# ========================================================
# Problem 3: (Excel handling):

# pip install pandas openpyxl
# pip install openpyxl
import pandas as pd

data = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Omar"],
    "Salary": [50000, 60000, 55000]
}
df = pd.DataFrame(data)

df.to_excel("employees.xlsx", index=False)

df_read = pd.read_excel("employees.xlsx")
print(df_read[['Name', 'Salary']])

# ========================================================
# Problem 4: (Data transformation):
import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = {"people": [row for row in reader]}
    
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"Converted {csv_file} to {json_file}")

csv_to_json("people.csv", "people.json")




