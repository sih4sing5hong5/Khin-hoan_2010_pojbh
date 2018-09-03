cj.inline_popup = {
	opener : null
	,_init : function(n){
		var ws = cj.util.getWindowSize();
		if(0 && n.set.pw > n.set.vp.w-50 || n.set.ph > ws.h - 50){
			cj.w.open(n.set.url, 'popup', 'width='+n.set.pw+25+'px,height='+n.set.ph+25+'px,status=1,location=1,resizable=1,scrollbars=1');
			return;
		}
		n.mask = cj.util.addElm(cj.d.body, [{ tag:'div', cssText:'position:absolute; top:0; left:0; background:#333; width:100%; height:100%', style:{opacity:0.8}}]);
		n.mask.onclick = function(){
			cj.inline_popup.close();
		}
		if(cj.isIE6) cj.util.ieMask(n.mask);
		n.pop = cj.util.addElm(cj.d.body, [{ tag : 'iframe', id : 'popup'+n.set.id, 'class' : 'popFrame', attrib:'frameBorder:0,src:javascript:"",scrollbars:no' }]);
		n.pop.setAttribute('src', n.set.url);
		n.setPos = function(){
			cj.inline_popup.setPos(this);
			cj.inline_popup.setPosition(this);
		}
		cj.inline_popup.pop = n.pop;
	}
	,setPos : function(n){
		n.set.vp = cj.util.getVP();
		n.set.pw = Math.min(n.set.vp.w, parseInt(n.set.w));
		//n.set.ph = Math.min(n.set.vp.h, parseInt(n.set.h)+130);
		n.set.ph = parseInt(n.set.h);
		n.set.x = Math.ceil((n.set.vp.w-n.set.pw)/2) + cj.util.getScrollPos().x;
		n.set.y = Math.max(cj.util.getScrollPos().y+20, Math.ceil((n.set.vp.h-n.set.ph)/2) + cj.util.getScrollPos().y);
	}
	,open : function(n, set){
		var t = this;
		n.set = set;
		this.setPos(n);
		t._init(n);
		t.opener = n;
		if(n.pop){
			this.setPosition(n);
		}
		cj.evt.add(cj.d, 'keypress', this.keypress);
	}
	,close : function(){
		var t = this;
		cj.util.setStyle(t.opener.pop, {visibility:'hidden', top:-10000, left:-10000});
		cj.util.setStyle(t.opener.mask, {visibility:'hidden', top:-10000, left:-10000});
		if(cj.isIE6) cj.util.setStyle(t.opener.mask.ieMask, {visibility:'hidden', top:-10000, left:-10000});
		cj.evt.remove(cj.w, 'keypress', t.opener.keypress);
	}
	,keypress : function(ev){
		var ev = ev || cj.w.event;
		var code = ev.which || ev.keyCode;
		if (code==27) cj.inline_popup.close();
	}
	,resize : function(n){

	}
	,setPosition : function(n){
		var ws = cj.util.getWindowSize();
		cj.util.setStyle(n.mask, {width:ws.w, height:ws.h, top:0, left:0, visibility:'visible'});
		cj.util.setStyle(n.pop, {width:n.set.pw,height:n.set.ph,left:n.set.x,top:n.set.y, visibility:'visible'});
		if(cj.isIE6) cj.util.setStyle(n.mask.ieMask, {
			width:n.mask.style.width
			,height:n.mask.style.height
			,left:n.mask.style.left
			,top:n.mask.style.top
			,visibility:'visible'
		});
	}
}