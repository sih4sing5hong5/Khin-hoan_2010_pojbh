cj.simpleMenu = {
	timer : null,
	items : [],
	openObj : null,
	ar : 0.99,
	init: function(menu, item, dir){
		var mm, sm;
		for (var i=0; i<menu.length; i++){
			mm = document.getElementById(menu[i]);
			sm = document.getElementById(item[i]);
			if (mm&&sm){
				mm.index = this.items.length;
				this.items[mm.index] = mm;
				mm.onmouseover = function(){ cj.simpleMenu.show(this.index)};
				mm.onmouseout = function(){ cj.simpleMenu.hide(this.index)};

				mm.div = document.createElement("div");
				mm.div.style.cssText = "position:absolute; visibility:hidden; z-index: 1000;";
				mm.div.style.top = cj.util.getElmPos(mm).y + mm.offsetHeight + "px";
				mm.div.style.left = cj.util.getElmPos(mm).x + "px";
				mm.div.style.width = sm.offsetWidth + "px";
				sm.style.top = "0px";
				sm.style.left = "0px";
				mm.appendChild(mm.div);
				mm.div.appendChild(sm);
				mm.index = i;

				var mask = document.createElement('iframe');
				mask.cssText = "position:absolute; display:none;";
				mask.style.border = "none";
				mask.style.width = sm.offsetWidth + 'px';
				mask.style.height = sm.offsetHeight + 'px';
				mask.style.top = mm.div.style.top;
				mask.style.left = mm.div.style.left;
				mm.div.appendChild(mask);
			}
		}
	},
	show : function(index){
		if(this.openObj){
			//this.openObj.div.style.display = 'none';
			this.openObj.div.style.visibility = 'hidden';
		}
		clearTimeout(this.timer);
		this.openObj = this.items[index];
		if(this.openObj){
			//this.openObj.div.style.display = 'block';
			this.openObj.div.style.visibility = 'visible';
		}
	},
	hide : function(index){
		var obj = this.items[index].div;
		if(obj) this.timer = setTimeout(function(){obj.style.visibility='hidden';}, 600);
	}
}