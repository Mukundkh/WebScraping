from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

with open('sample.html') as html_file:
    soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

print(article.prettify())
for article in soup.find_all('div', class_='article'):

    # print(article)

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)
# print(vid_src)

yt_link = f"https://youtube.com/watch?v={vid_id}"
print(yt_link)
 
