# ========================================================
# Problem 1: (Fetch a web page title):

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(f"Page Title: {soup.title.string}")


# ========================================================
# Problem 2: (Extract All Links):

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
for link in links:
    href = link.get('href')
    if href:
        print(href)


# ========================================================
# Problem 3: (Extract a table):

from bs4 import BeautifulSoup

html = """
<table>
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>25</td></tr>
    <tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

for row in rows:
    cols = row.find_all(['td', 'th'])
    row_data = [col.text for col in cols]
    print(row_data)

# ========================================================
# Problem 4: (Automate google search):

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Web Scraping")
search_box.send_keys(Keys.RETURN)
    
print("Page title:", driver.title)
driver.quit()


# ========================================================
# Problem 5: (save scarped data csv):

import csv
from bs4 import BeautifulSoup

html = """
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')
fruits = [li.text for li in soup.find_all('li')]

with open('fruits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit'])  # Header
    for fruit in fruits:
        writer.writerow([fruit])

print("Data saved to fruits.csv")