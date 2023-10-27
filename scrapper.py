import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.get_text()  # Get only text
    print(search_results)
else:
    print('Error:', response.status_code)
