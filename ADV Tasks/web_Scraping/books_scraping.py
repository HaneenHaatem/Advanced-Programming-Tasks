from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")

time.sleep(2)

data = [("Title", "Price")]

books = driver.find_elements(By.CLASS_NAME, "product_pod")

for book in books:
    title = book.find_element(By.TAG_NAME, "h3").text.strip()
    price = book.find_element(By.CLASS_NAME, "price_color").text.strip()
    data.append((title, price))

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Saved to books.csv")

driver.quit()
