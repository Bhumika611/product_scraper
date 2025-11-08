# 🛒 Books-to-Scrape Product Scraper

A small, internship-friendly Python scraper that extracts product details (book name, price, and rating) from the demo website **Books to Scrape** and saves the results to a CSV file.

This repository contains a simple and readable script (no external API keys or complex setup) — perfect for demonstrations, learning web scraping basics, and adding to your GitHub portfolio.


### PowerShell one-liner — create `README.md` automatically
Open PowerShell in your `product_scraper` folder and paste this (it writes the file exactly as above):

```powershell
$readme = @'
# 🛒 Books-to-Scrape Product Scraper

A small, internship-friendly Python scraper that extracts product details (book name, price, and rating) from the demo website **Books to Scrape** and saves the results to a CSV file.

This repository contains a simple and readable script (no external API keys or complex setup) — perfect for demonstrations, learning web scraping basics, and adding to your GitHub portfolio.


## 🔧 Requirements
- Python 3.x
- Libraries:
  ```bash
  py -m pip install requests beautifulsoup4

⚙️ How to run

1. Open terminal / PowerShell and navigate to the project folder:

cd C:\Users\bhumi\OneDrive\bhumi\product_scraper

2. Run the script:

py product_scraper.py


The script prints progress messages and creates products.csv in the same folder.

🧾 Example output (products.csv)
Name	Price	Rating
A Light in the Attic	£51.77	Three
Tipping the Velvet	£53.74	One
Soumission	£50.10	One

(Actual values depend on the site content at run time.)

📝 Notes & tips

This demo site (books.toscrape.com) is intended for learning and practice — it does not block scrapers, so it’s perfect for internship demos.

If you want to expand the scraper:

Add pagination to scrape multiple pages.

Save additional fields (availability, product page URL).

Store results in JSON or a SQLite database.

Add logging and better error handling.

Respect robots.txt and site terms for real-world sites; avoid scraping protected/commercial websites without permission.

🚀 Improvements you can add (good internship talking points)

Add a CLI flag to specify page number or number of pages to scrape.

Add retry logic and exponential backoff for network errors.

Normalize prices (convert £ to numbers) and map textual ratings (Three) to numeric (3).

Create a small unit test for the extract_books function using saved HTML samples.


👩‍💻 Author

Bhumika Macharla — Internship project
GitHub: Bhumika611