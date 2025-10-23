import requests
from bs4 import BeautifulSoup

#Taking URL of website as Input
URL = input("Enter the News Website URL : ")

#Fetching HTML content
response = requests.get(URL)
html_content = response.text

#Parsing HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

#Finding H2 headline tags
headlines = soup.find_all('h2')

#Extracting and cleaning the text
news_headlines = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:  # avoid empty lines
        news_headlines.append(text)

#Saving headlines into a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(news_headlines, start=1):
        file.write(f"{i}. {headline}\n")

print("✅ Headlines scraped and saved to 'headlines.txt'")
