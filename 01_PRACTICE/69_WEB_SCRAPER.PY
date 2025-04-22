import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the headings (for example)
for heading in soup.find_all(['h1', 'h2', 'h3']):
    print(heading.get_text())