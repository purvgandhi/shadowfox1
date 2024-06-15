import requests
from bs4 import BeautifulSoup


url = 'https://www.geeksforgeeks.org/'

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')


articles = soup.find_all('div', class_='top-first-post')

for article in articles:
    title = article.find('div', class_='head').text.strip()
    link = article.find('a')['href']
    summary = article.find('p').text.strip()

    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Summary: {summary}')
    print()
