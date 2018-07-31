from itertools import chain
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
        if '-99.' not in sootsai:
            continue
        with open(sootsai) as tong:
            soup = BeautifulSoup(tong, 'lxml')
            tailo = list(chhue(soup.find(id='artical_tailo')))
            hanlo = list(chhue(soup.find(id='artical_content')))

            if len(tailo) != len(hanlo):
                print(sootsai)
                print(len(tailo), len(hanlo))
                for a, b in zip(tailo, hanlo):
                    print(a, b)
                break

#             print(sootsai)
            chu = laiiong(soup)
            chu[tailo]=tailo
            chu[hanlo]=hanlo
            yield chu
#             break


def laiiong(soup):
    chu = {}
    for td in laiiong_td(soup):
        kiatko = td.get_text()
        if kiatko != '':
            na, iong = kiatko.split('：', 1)
            chu[na] = iong
    return chu


def laiiong_td(soup):
    chuiau = soup.find("table", attrs={"style": "text-align:left"})
    yield from chuiau.find_all('td')

    for thann in chuiau.parent.parent.find_next_siblings('tr'):
        for td in thann.find_all('td'):
            yield td


def chhue(span):
    for tuann in chhue_p(span):
        kiatko = tuann.strip()
        if kiatko:
            yield kiatko


def chhue_p(span):
    for p in span.find_all('p'):
        tuann = []
        for tanui in p.children:
            chhiat = False
            try:
                for ete in chain([tanui], tanui.descendants):
                    try:
                        if ete.name == 'br':
                            chhiat = True
                    except AttributeError:
                        pass
            except AttributeError:
                pass
            if chhiat:
                yield ''.join(tuann)
                tuann = []

            try:
                string = tanui.get_text()
            except AttributeError:
                string = tanui
            tuann.append(string)
        yield ''.join(tuann)


if __name__ == '__main__':
    tsuliau()
