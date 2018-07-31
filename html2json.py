from os.path import join
from posix import listdir
import re

from bs4 import BeautifulSoup


def tsanpootong():
    boklok = join('pojbh.lib.ntnu.edu.tw', 'script')
    buntsiunn = re.compile('artical-\d+.htm')
    for mia in sorted(listdir(boklok)):
        if buntsiunn.match(mia):
            yield join(boklok, mia)


def tsuliau():
    for sootsai in tsanpootong():
        if '2260' not in sootsai:
            continue
        with open(sootsai) as tong:
            soup = BeautifulSoup(tong, 'lxml')
            tailo = list(chhue(soup.find(id='artical_tailo')))
            hanlo = list(chhue(soup.find(id='artical_content')))

            print(len(tailo), len(hanlo))
            if len(tailo)!= len(hanlo):
                print(sootsai)

            chu = laiiong(soup)
            break


def laiiong(soup):
    chu = {}
    for td in laiiong_td(soup):
        kiatko = td.get_text()
        if kiatko != '':
            na, iong = kiatko.split('：')
            chu[na] = iong
    return chu


def laiiong_td(soup):
    chuiau = soup.find("table", attrs={"style": "text-align:left"})
    yield from chuiau.find_all('td')

    for thann in chuiau.parent.parent.find_next_siblings('tr'):
        for td in thann.find_all('td'):
            yield td


def chhue(span):
    yield from span.stripped_strings


tsuliau()
