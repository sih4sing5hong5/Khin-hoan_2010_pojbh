time wget -k -p -r -l inf -E http://pojbh.lib.ntnu.edu.tw

	new file:   pojbh.lib.ntnu.edu.tw/images/nav_about_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/images/nav_collection_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/images/nav_forum_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/images/nav_news_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/images/nav_plant_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/images/nav_sitemap_ov.gif
	new file:   pojbh.lib.ntnu.edu.tw/js/cj/inline_popup.js
	new file:   pojbh.lib.ntnu.edu.tw/js/cj/res/cj.css
	new file:   pojbh.lib.ntnu.edu.tw/js/cj/roller.js
	new file:   pojbh.lib.ntnu.edu.tw/js/cj/simpleMenu.js


  900  cat window | sed "s/.*window.open('/http:\/\/pojbh.lib.ntnu.edu.tw\/script\//g" | sed "s/', 'artical.*//g" | tee wget_src_html
