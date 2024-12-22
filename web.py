import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce website's product page (example: Books to Scrape)
url = "http://books.toscrape.com/"

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all product elements
products = soup.find_all(class_="product_pod")

# List to store product details
product_list = []

# Extract product details
for product in products:
    name = product.h3.a["title"]
    price = product.find(class_="price_color").get_text(strip=True)
    rating = product.p["class"][1]  # 'star-rating' and actual rating class (e.g., 'Three')
    product_list.append([name, price, rating])

# Create a DataFrame and save to CSV
df = pd.DataFrame(product_list, columns=["Name", "Price", "Rating"])
df.to_csv("products.csv", index=False, encoding="utf-8")

print("Product data extracted and saved to products.csv")
