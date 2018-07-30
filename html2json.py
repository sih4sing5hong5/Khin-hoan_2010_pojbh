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

            'style="text-align:left"'
            print(len(tailo),len(hanlo))
            break


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
