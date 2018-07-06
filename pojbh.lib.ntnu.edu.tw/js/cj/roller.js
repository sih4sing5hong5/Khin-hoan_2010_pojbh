	cj.roller = {
		init : function(boxid, itemcontainerid, rollerSet){
			var box = document.getElementById(boxid);
			if (!box){
				return;
			}
			var items = document.getElementById(itemcontainerid);
			if(!items)	return;
			box.items = items.getElementsByTagName('table');
			if(!box.items || !box.items.length){
				return;
			}
			box.index = 0;
			box.timer = null;
			rollerSet.showNum = Math.min(box.items.length, rollerSet.showNum);
			box.rollerSet = rollerSet;
			box.doRoll = (box.items.length > box.rollerSet.showNum);
			
			var div = document.createElement("div");
			div.style.cssText = "position:absolute; top:0px; left:0px; visibility:visible;";
			box.divs = [];
			for (var i=0; i<=rollerSet.showNum; i++){
				box.divs[i] = div.cloneNode(true);
				box.appendChild(box.divs[i]);
				box.divs[i].style.top = '1px';
				box.divs[i].style.left = '1px';
			}
			this.roll(box);
			if(box.doRoll){
				box.onmouseover = function(){
					clearTimeout(box.timer);
				}
				box.onmouseout = function(evt){
					var evt = evt || window.event;
					var related = evt.relatedTarget || evt.toElement;
					var contains = false;
					while(related){
						if(related == this){
							contains = true;
							break;
						}
						related =  related.offsetParent;
					}
					if(!contains){
						box.timer = cj.roller.rollNext(box);
					}
				}
			}
		},
		roll : function(obj){
			for(var i=0; i<=obj.rollerSet.showNum; i++){
				while(obj.divs[i].childNodes[0]){
					obj.divs[i].removeChild(obj.divs[i].childNodes[0]);
				}
				obj.divs[i].appendChild(obj.items[(obj.index+i)%obj.items.length].cloneNode(true));
				if (i){
					if (obj.rollerSet.dir == "horizontal"){
						obj.divs[i].style.left = obj.divs[i-1].offsetLeft + obj.divs[i-1].offsetWidth + obj.rollerSet.gap + "px";
					}else{
						obj.divs[i].style.top = obj.divs[i-1].offsetTop + obj.divs[i-1].offsetHeight + obj.rollerSet.gap + "px";
					}
				}else{
					obj.divs[i].style.top = obj.divs[i].style.left = 1 + "px";
				}
				if (i == obj.rollerSet.showNum){
					obj.divs[i].style.visibility = "hidden";
				}
			}
			if(obj.doRoll){
				obj.index  = (obj.index == obj.items.length -1) ? 0 : obj.index +1;
				obj.timer = setTimeout(function(){cj.roller.rollNext(obj)}, obj.rollerSet.holdtime * 1000);
			}
		},
		rollNext : function(obj){
			for(var i=0; i<=obj.rollerSet.showNum; i++){
				obj.divs[i].style.visibility = "visible";
				if (obj.rollerSet.dir == "horizontal"){
					obj.divs[i].style.left = obj.divs[i].offsetLeft - obj.rollerSet.step + "px";
				}else{
					obj.divs[i].style.top = obj.divs[i].offsetTop - obj.rollerSet.step + "px";
				}
			}
			if(obj.divs[1].offsetLeft<0 || obj.divs[1].offsetTop<0){
				this.roll(obj);
			}else{
				obj.timer = setTimeout(function(){cj.roller.rollNext(obj)}, obj.rollerSet.rolltime);
			}
		}
	}