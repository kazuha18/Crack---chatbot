import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
    page=1
    while page <= max_pages:
        url="https://www.programiz.com/c-programming#tutorial"+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        url=soup.find_all('a')
        for urls in url:
            print("https://www.programiz.com/c-programming"+urls.get('href'))

            page+=1

def trade_spider2(max_pages):
    page=1
    while page <= max_pages:
        url="https://www.programiz.com/cpp-programming"+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"lxml")
        url=soup.find_all('a')
        for urls in url:
            print("https://www.programiz.com/cpp-programming"+urls.get('href'))

            page+=1

def trade_spider3(max_pages):
    page=1
    while page <= max_pages:
        url="https://www.programiz.com/java-programming"+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"lxml")
        url=soup.find_all('a')
        for urls in url:
            print("https://www.programiz.com/java-programming"+urls.get('href'))

            page+=1


def trade_spider4(max_pages):
        page = 1
        while page <= max_pages:
            url = "https://www.programiz.com/dsa" + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            url = soup.find_all('a')
        for urls in url:
            print("https://www.programiz.com/dsa" + urls.get('href'))

            page += 1


def trade_spider5(max_pages):
    page = 1
    while page <= max_pages:
        url = "hhttp://www.inteliclass.com/blog/notes-on-database-management-system-ibps-so-it-professional/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        url = soup.find_all('a')
    for urls in url:
        print("http://www.inteliclass.com/blog/notes-on-database-management-system-ibps-so-it-professional/" + urls.get('href'))

        page += 1

def trade_spider6(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://ecomputernotes.com/computernetworkingnotes" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        url = soup.find_all('a')
    for urls in url:
        print("http://ecomputernotes.com/computernetworkingnotes" + urls.get('href'))

        page += 1
