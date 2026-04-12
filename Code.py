import requests
from bs4 import BeautifulSoup
import pandas as pd


# Step1: Choose a target URL (using a public books site as example)
URL = "https://books.toscrape.com/"

# Step2: Send HTTP request
headers = {"User-Agent": "Mozilla/5.0"}   # pretend to be a browser
response = requests.get(URL,headers=headers)

# Step3: Parse the HTML
soup = BeautifulSoup(response.content,"html.parser")

# Step4: Find the data you want (book title + prices)
books = soup.find_all("article",class_="product_pod")

data=[]
for book in books:
    title = book.h3.a["title"]     # get book title
    price = book.find("p",class_="price_color").text.strip()
    rating = book.p["class"][1]                  # e,g. "Three","Five"
    data.append({"Title":title, "Price":price, "Rating": rating})

# Step5: Save to CSV
df = pd.DataFrame(data)
df.to_csv("scraped_books.csv",index=False)
print(df)
print(f"\n Scraped {len(df)} books and saved to scraped_books.csv")
