import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok = True)


print (f'Downloading page {url}....')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

comicElim = soup.select('#comic img')
if comicElim == []:
    print('could not find comic image')
else:
    comicURL = "https:" +comicElim[0].get('src')
    print(f'Downloading image {comicURL}')
    res = requests.get(comicURL)
    res.raise_for_status()
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
    for chunk in res.iter_content():
        imageFile.write(chunk)
    imageFile.close()