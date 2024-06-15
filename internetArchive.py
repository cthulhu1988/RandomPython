import os, shlex
import requests
import wget
from bs4 import BeautifulSoup

url = 'https://archive.org/download/the-magic-school-bus-full-series-dvd-rip/Season%201/'

def downloadWho(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        vid = (link.get('href'))
        vid = str(vid)
        if (vid[-1]) == '4' or (vid[-1] == 'v'):
            if(vid[-2] != 'k'):
                fullURL = url + '/' + vid
                os.system(f"wget -c --read-timeout=5 --tries=0 {shlex.quote(fullURL)}")
                #print(vid)
                #print(fullURL)

if __name__ == "__main__":
    downloadWho(url)





