from os.path import join
from posix import listdir
import re

from bs4 import BeautifulSoup


def tsanpootong():
    boklok = join('pojbh.lib.ntnu.edu.tw', 'script')
    buntsiunn = re.compile('artical-(\d+).htm')
    for mia in sorted(listdir(boklok)):
        tuiing = buntsiunn.match(mia)
        if tuiing:
            yield tuiing.group(1), join(boklok, mia)


def tsuliau():
    for pianho, sootsai in tsanpootong():
#         if '-12789.' not in sootsai:
#             continue
        with open(sootsai) as tong:
            soup = BeautifulSoup(tong, 'lxml')
            tailo = list(chhue(soup.find(id='artical_tailo')))
            hanlo = list(chhue(soup.find(id='artical_content')))

            if len(tailo) != len(hanlo):
                print(sootsai)
                print(len(tailo), len(hanlo))
#                 for a, b in zip(tailo, hanlo):
#                     print(a, b)
#                     print()
#                 break

            chu = laiiong(soup)
            chu['pianho'] = pianho
            chu['tailo'] = tailo
            chu['hanlo'] = hanlo
            yield chu


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
    for p in span.children:
        try:
            p.name
        except AttributeError:
            print('p', p.strip())
            yield p.strip()
        else:
            tuann = []
            for chiat in chhue_p_ete(p):
                if chiat is not True:
                    tuann.append(chiat)
                else:
                    yield ''.join(tuann)
                    tuann = []
            yield ''.join(tuann)


def chhue_p_ete(p):
    try:
        for ete in p.children:
            yield from chhue_p_ete(ete)
        if p.name in['p', 'br']:
            yield True
    except AttributeError:
        if '\n' == p:
            yield True
        else:
            yield p


if __name__ == '__main__':
    list(tsuliau())
