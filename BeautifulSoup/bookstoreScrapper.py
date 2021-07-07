from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd


pages = []
prices = []
stars = []
titles = []
urlss = []

pages_to_scrape = 2

for i in range(1, pages_to_scrape+1):
    url = ('http://books.toscrape.com/catalogue/page-{}.html'.format(i))
    pages.append(url)
    # print(pages)
for page in pages:
    page = requests.get(page)
    soup = bs4(page.text, 'html.parser')
    for i in soup.findAll('h3'):
        ttl = i.getText()
        titles.append(ttl)
    for j in soup.findAll('p', class_='price_color'):
        price = j.getText()
        prices.append(price)
    for k in soup.findAll('p', class_='star-rating'):
        for k, v in k.attrs.items():
            star = v[1]
            stars.append(star)
            # print(stars)
    divs = soup.findAll('div', class_='image_container')
    for thumbs in divs:
        tgs = thumbs.find('img', class_='thumbnail')
        urls = 'http://books.toscrape.com/'+str(tgs['src'])
        newurls = urls.replace("../", "")
        urlss.append(newurls)
        # print(urls)
data = {'Title': titles, 'Prices': prices, 'Stars': stars, "URLS": urlss}
df = pd.DataFrame(data=data)
df.index += 1
df.to_excel("output.xlsx")
