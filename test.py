from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

f='flora of uzbekistan'
a = 'https://www.google.com/search?q=' + '+'.join(f.split(' '))
a = 'https://suntravel.uz/flora-and-fauna'
print(a)

req = Request(
    url=a,
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()


soup = BeautifulSoup(webpage, 'html.parser')

for link in soup.find_all('a', href=True):
    z = link['href'].find('&sa')
    if '/url?q=' in link['href']:
        print(link['href'][7:z])
        link['href'] = '/result/{{'+str(link['href'])+'}}'
    print(link['href'])
print(soup)