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
            tailo = soup.find(id='artical_tailo').find('span')
#             print(tailo.get_text)
            print(tailo.contents)
            for a in (tailo.children):
                print('xx')
                print(a.contents)
            break

        'artical_content'
        'style="text-align:left"'


tsuliau()
