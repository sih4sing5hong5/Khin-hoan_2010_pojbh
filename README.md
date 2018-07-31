# 台灣白話字文獻館
[![Build Status](https://travis-ci.org/Taiwanese-Corpus/Khin-hoan_2010_pojbh.svg?branch=master)](https://travis-ci.org/Taiwanese-Corpus/Khin-hoan_2015_pojbh)

很感謝您瀏覽及使用「[台灣白話字文獻館](http://pojbh.lib.ntnu.edu.tw/script/news-p0.htm)」。本資料庫之內容，除另註明，皆採用[「CC授權條款」（Creative Commons）](http://creativecommons.org.tw/)。主要文字皆為數位典藏國家型科技計畫、國立台灣師範大學台灣文化及語言文學研究所所有，圖片則分別授權自台灣教會公報社、台灣基督教長老教會教會歷史委員會、北部台灣基督教長老教會史蹟委員會（真理大學牛津學堂），以及淡江中學校史館。所有權利若無特別說明，皆屬版權所有。

- 計劃執行時間：2007-2010
- 鏡像[gh-page](https://taiwanese-corpus.github.io/Khin-hoan_2010_pojbh/)。

### 資料來源


#### Json格式資料
`pojbh.json`是自`pojbh.lib.ntnu.edu.tw/`原始網站整理出來--的。
```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
python html2json.py
```

#### 原始網站
自`pojbh.lib.ntnu.edu.tw/`掠落來--的。
```
time wget -k -p -r -l inf -E http://pojbh.lib.ntnu.edu.tw
```
因為有的資源用js import，wget以外閣需要另外處理
```
# 看原圖的網頁
grep window.open\( pojbh.lib.ntnu.edu.tw/script/ -r | 、
  sed "s/.*window.open('/http:\/\/pojbh.lib.ntnu.edu.tw\/script\//g" | 、
  sed "s/', 'artical.*//g"
# js需要的靜態資料
pojbh.lib.ntnu.edu.tw/images/nav_about_ov.gif
pojbh.lib.ntnu.edu.tw/images/nav_collection_ov.gif
pojbh.lib.ntnu.edu.tw/images/nav_forum_ov.gif
pojbh.lib.ntnu.edu.tw/images/nav_news_ov.gif
pojbh.lib.ntnu.edu.tw/images/nav_plant_ov.gif
pojbh.lib.ntnu.edu.tw/images/nav_sitemap_ov.gif
pojbh.lib.ntnu.edu.tw/js/cj/inline_popup.js
pojbh.lib.ntnu.edu.tw/js/cj/res/cj.css
pojbh.lib.ntnu.edu.tw/js/cj/roller.js
pojbh.lib.ntnu.edu.tw/js/cj/simpleMenu.js
```