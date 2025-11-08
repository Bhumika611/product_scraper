import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def get_html(url):
    """Fetch page HTML with random user agent"""
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ])
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print("Failed to fetch page:", response.status_code)
        return None


def extract_books(soup):
    """Extract product name, price, and rating"""
    books = []
    items = soup.find_all("article", class_="product_pod")
    for item in items:
        name = item.h3.a["title"]
        price = item.find("p", class_="price_color").text.strip()
        rating = item.p["class"][1] if len(item.p["class"]) > 1 else "N/A"

        books.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })
    return books


def save_to_csv(data, filename="products.csv"):
    """Save extracted data into a CSV file"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Price", "Rating"])
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Data saved successfully to {filename}")


def main():
    print("Fetching product data from Books to Scrape... please wait!\n")
    time.sleep(random.randint(1, 3))

    url = "https://books.toscrape.com/catalogue/page-1.html"
    soup = get_html(url)
    if soup:
        products = extract_books(soup)
        if products:
            save_to_csv(products)
            print(f"Extracted {len(products)} products successfully.")
        else:
            print("No products found.")
    else:
        print("Unable to fetch data.")


if __name__ == "__main__":
    main()
