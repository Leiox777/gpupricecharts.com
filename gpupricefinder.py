import requests
from bs4 import BeautifulSoup
import numpy as np
import regex
import matplotlib.pyplot as plt

data = []
times = []
users = []
#USER_INPUT=================================================
search = input("GPU Search>")
search = search.replace(" ", "+")
print(search)
#USER_INPUT=================================================

def clean(price):
    return regex.sub("[^0-9]","",price)

#REQUESTS===================================================
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
print('http://www.watchcount.com/completed.php?bkw={}&bcat=0&bcts=&sfsb=Show+Me%21&csbin=all&cssrt=ts&bfw=1&bslr=&bnp=&bxp=#serp'.format(search))
html = requests.get('http://www.watchcount.com/completed.php?bkw={}&bcat=0&bcts=&sfsb=Show+Me%21&csbin=all&cssrt=ts&bfw=1&bslr=&bnp=&bxp=#serp'.format(search),headers=headers)
soup = BeautifulSoup(html.text)
#REQUESTS===================================================

#PARSEING==UNSTABLE=========================================
for hit in soup.findAll(attrs={'class' : 'padr2 bhserp-txt1 bhserp-new1'}):
    data.append(int(clean(hit.text)))

index = 0
for hit in soup.findAll('span',attrs={'class' : 'bhserp-dim2'}):
    if index == 0:
        times.append(hit.text)
        index += 1
    else:
        users.append(hit.text)
        index -= 1
#PARSEING===================================================

# splittablecell1

finalarray = np.array([data,users,times])
print(finalarray)
print("times range: ",range(len(times)))

x = range(len(times))

plt.plot(data,'r')
plt.show()
