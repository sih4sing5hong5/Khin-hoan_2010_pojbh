from unittest.case import TestCase

from bs4 import BeautifulSoup
from html2json import laiiong


class chhigiam(TestCase):
    def test_2260(self):
        chu = laiiong(BeautifulSoup(self.artical2260, 'lxml'))
        self.assertEqual(
            chu, {
                '卷期': '第373卷',
                '本次': '',
                '日期': '1916/4',
                '刊名': '台灣教會報',
                '頁數': '6',
                '篇名': '葉俊ê小傳 [ Ia̍p tsùn ê Sió-toān ]',
                '作者': '葉金木 Ia̍p Kim-bo̍k'

            }
        )

    artical2260 = '''<table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td align="left"><table border="0" cellspacing="0" cellpadding="0">
                          <tr>
                            <td><table width="100%" border="0" cellspacing="0" cellpadding="0" style="text-align:left">
                                <tr>
                                  <td class="gy12">卷期：第373卷</td>
                                  <td><img src="../images/spacer.gif" width="20" height="5" border="0"></td>
                                  <td class="gy12">本次：</td>
                                  <td><img src="../images/spacer.gif" width="20" height="5" border="0"></td>
                                  <td class="gy12">日期：1916/4</td>
                                  <td><img src="../images/spacer.gif" width="20" height="5" border="0"></td>
                                  <td class="gy12">刊名：台灣教會報</td>
                                  <td><img src="../images/spacer.gif" width="20" height="5" border="0"></td>
                                  <td class="gy12">頁數：6</td>
                                </tr>
                              </table></td>
                          </tr>
                          <tr>
                            <td class="gy12" align="left">篇名：葉俊ê小傳 [ Ia̍p tsùn ê Sió-toān ]</td>
                          </tr>
                          <tr>
                            <td class="gy12" align="left">作者：葉金木 Ia̍p Kim-bo̍k</td>
                          </tr>
                      </table>'''
