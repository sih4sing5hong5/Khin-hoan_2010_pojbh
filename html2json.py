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

            print(list(laiiong(soup)))
            break


def laiiong(soup):
    for td in laiiong_td(soup):
        kiatko = td.get_text()
        if kiatko != '':
            yield kiatko


def laiiong_td(soup):
    chuiau = soup.find("table", attrs={"style": "text-align:left"})
    yield from chuiau.find_all('td')

    for thann in chuiau.parent.parent.find_next_siblings('tr'):
        for td in thann.find_all('td'):
            yield td


def chhue(span):
    for p in (span.find_all('p')):
        for ku in p.contents:
            yield from chuan(ku)


def chuan(htmltag):
    try:
        for ku in htmltag.contents:
            yield from chuan(ku)
    except AttributeError:
        yield htmltag


tsuliau()
