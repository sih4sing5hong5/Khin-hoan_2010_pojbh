cj = {
	 version : '1.0'
	,modify : '2009/04/17'

	,files : {}
	,elm : []

	,init : function(set){
		var t = this,  na = navigator, ua = na.userAgent, src, ss;
		t.d = document;
		t.w = window;
		t.b = t.d.documentElement || t.d.body;

		t.isOpera = t.w.opera && opera.buildNumber;
		t.isWebKit = /WebKit/.test(ua);
		t.isIE = !t.isWebKit && !t.isOpera && (/MSIE/gi).test(ua) && (/Explorer/gi).test(na.appName);
		t.isIE6 = t.isIE && /MSIE [56]/.test(ua);
		t.isGecko = !t.isWebKit && /Gecko/.test(ua);
		t.isMac = ua.indexOf('Mac') != -1;
		t.isAir = /adobeair/i.test(ua);

		ss = document.getElementsByTagName('script');
		for(var i=0, l=ss.length; i<l; i++){
			src = ss[i].src;
			if(src && /cj\.js/.test(src)){
				t.base = src.substring(0, src.lastIndexOf('/')) + '/';
				break;
			}
		}
		if(set&&set.require){
			t.util.each(set.require.split(','), function(s){
				if(t.files[s]) return;
				t.files[s] = true;
				s = t.base + s + '.js';
				t.util.loadJs(s);
			});
		}
		t.util.loadCss(t.base + 'res/cj.css');
		t.vp = t.util.getVP();
	}
    ,evt : {
		 guid : 1
		,add : function (elm, type, handler){
			if(elm.addEventListener){
				elm.addEventListener(type, handler, false);
			}else if (elm.attachEvent){
				elm.attachEvent('on' + type, handler);
			}else{
				if (!handler.$$guid){
					handler.$$guid = this.guid++;
				}
				if (!elm.events){
					elm.events = {};
				}
				var handlers = elm.events[type];
				if (!handlers){
					handlers = elm.events[type] = {};
					if(elm['on' + type]){
						handlers[0] = elme['on' + type];
					}
				}
				handlers[handler.$$guid] = handler;
				elm['on' + type] = this.handleEvent;
			}
			return handler;
		}
		,remove : function(elm, type, handler){
			if (elm.removeEventListener){
				elm.removeEventListener(type, handler, false);
			}else{
				if (elm.events && elm.events[type]){
					delete elm.events[type][handler.$$guid];
				}
			}
		}
		,cancel : function(ev){
			ev.cancelBubble = true;
			if(ev.stopPropagation){
				ev.stopPropagation();
			}
		}
	}
	,util : {
		is : function(o, type){
			return (typeof o == type);
		}
		,getMousePos : function(ev){
			return (ev.pageX && ev.x) ? {'x':ev.pageX, 'y':ev.pageY} : {'x':ev.clientX+this.getScrollPos().x, 'y':ev.clientY+this.getScrollPos().y}
		}
		,getScrollPos : function(){
			return {
				x : document.documentElement.scrollLeft || document.body.scrollLeft
				,y : document.documentElement.scrollTop || document.body.scrollTop
			}
		}
		,getWindowSize : function(){
			var b = cj.d.documentElement || cj.d.body;
			return { w:b.scrollWidth, h:b.scrollHeight}
		}
		,getSize : function(n) {
			var t = this, w, h;
			w = n.style.width;
			h = n.style.height;
			if (w.indexOf('px') === -1) w = 0;
			if (h.indexOf('px') === -1) h = 0;
			return {
				w : parseInt(w) || n.offsetWidth || n.clientWidth,
				h : parseInt(h) || n.offsetHeight || n.clientHeight
			};
		}
		,getVP : function(){
			return {
				x : cj.w.pageXOffset || cj.b.scrollLeft,
				y : cj.w.pageYOffset || cj.b.scrollTop,
				w : cj.w.innerWidth || cj.b.clientWidth,
				h : cj.w.innerHeight || cj.b.clientHeight
			}
		}
		,getElmSize : function(n){
			return {
				w : n.clientWidth
				,h : n.clientHeight
			}
		}
		,getPos : function(n){
			var x = y = 0;
	   		while(n){
	   			if(n.style.left) return{x:parseInt(n.style.left)||0, y:parseInt(n.style.top)||0}
	   			if(n.style.left){
	   				x += parseInt(n.style.left)||0;
	   				y += parseInt(n.style.top)||0;
	   				break;
	   			}else{
	   				x += n.offsetLeft;
		   			y += n.offsetTop;
		   		}
	   			n = n.offsetParent;
	   		}
	   		return {x:x,y:y};
	   	}
	   	,getElmPos : function(n){
			var x = y = 0;
	   		while(n){
	   			x += n.offsetLeft;
		   		y += n.offsetTop;
	   			n = n.offsetParent;
	   		}
	   		return {x:x,y:y};
	   	}
		,getAbsPos : function(n){
			return { x:parseInt(n.style.left)||0, y:parseInt(n.style.top)||0}
	   	}
	   	,setStyle : function(n, set){
	   		var s = n.style;
	   		for(var k in set){
	   			v = set[k];
	   			switch(k){
	   				case 'opacity':
	   					this.setOpacity(n, v);
	   				break;
	   				case 'zIndex':
	   					s.zIndex = v;
	   				break;
	   				default :
	   					if(cj.util.is(v, 'number') || /^[\-0-9\.]+$/.test(v)) v += 'px';
	   					s[k] = v;
	   				break;
	   			}
			}
	   	}
		,fix_ieflash : function() {
			var objects = document.getElementsByTagName('object');
			for (var i=0;i<objects.length;i++)
				objects[i].outerHTML = objects[i].outerHTML;
		}
		,loadJs : function(s){
		   	var h = document.getElementsByTagName('head')[0];
		   	o = this.addElm(h, [{tag : 'script', attrib : 'type:text/javascript;src:'+s}]);
		}
		,loadCss : function(u){
			var u = u || ''
			var h = document.getElementsByTagName('head')[0]
			this.each(u.split(','), function(u){
				if(cj.files[u]) return;
				cj.files[u] = true;
				cj.util.addElm(h, {tag:'link',attrib:'rel:stylesheet;type:text/css;href:'+u});
			});
		}
		,addElm : function(p, set){
			var i, o, t = this;
			if(t.is(set,'string') || !set.length){
				o = p.appendChild(this.createElm(set));
			}else{
				o = p.appendChild(t.createElm(set[0]));
				for(var i=1, l=set.length; i<l; i++){
					t.addElm(o, set[i]);
				}
			}
			return o;
		}
		,createElm : function(set){
			var o, a , s, d = document, t = this;
			o = t.is(set, 'string')
				? d.createTextNode(set)
				: d.createElement(set.tag);
			if(set.id){
				o.id = set.id;
				cj.elm[set.id] = o;
			}
			if(set.cssText) o.style.cssText = set.cssText;
			if(set['class']){
				o.className = set['class'];
			}
			if(set.innerHTML) o.innerHTML = set.innerHTML;
			if(set.style) t.setStyle(o, set.style);
			if(set.attrib){
				cj.util.each(set.attrib.split(';'), function(s){
					if(s.indexOf(':') != -1){
						n = s.indexOf(':');
						k = s.substr(0, n).replace(/\s+/g);
						v = s.substr(n+1, s.length);
						o.setAttribute(k, v)
					}
				});
			}
			return o;
		}
		,removeChild : function(n){
			if(n.firstChild){
				while(n.firstChild){
					if(n.firstChild.firstChild) removeAllChild(n.firstChild);
					else n.removeChild(n.firstChild);
				}
			}
			n.parentNode.removeChild(n);
		}
		,setOpacity : function(o, v){
			if(!o){
				alert('setOpacity : o is nto defined');
				return;
			}
			if(v<0.1){
				o.style.display = 'none';
				return;
			}
			if(typeof o.style.opacity != 'undefined'){
				o.style.opacity = (v == 1) ? 0.9999999 : v;
			}else if (typeof o.style.MozOpacity != 'undefined'){
				o.style.MozOpacity = (v == 1) ? 0.9999999 : v;
			}else if (typeof o.style.KhtmlOpacity != 'undefined'){
				o.style.KhtmlOpacity = v;
			}else{
				o.style.filter = 'alpha(opacity=' + Math.floor(v*100) + ')';
			}
		}
		,each : function(o, cb, s){
			if(!o)
				return 0;
			s = s || o;
			if(typeof(o.length) != 'undefined'){
				for(var i=0, l=o.length; i<l; i++){
					if(cb.call(s, o[i], i, o) === false)
						return 0;
				}
			}else{
				for (var i in o){
					if(o.hasOwnProperty(i)){
						if(cb.call(s, o[i], i, o) === false){
							return 0;
						}
					}
				}
			}
			return 1;
		}
		,ieMask : function (n){
			if(!cj.isIE6) return null;
			var t = this, s = n.style, ieMask;
			ieMask = t.addElm(cj.d.body, {tag:'iframe','class':'cjIEMask',attrib:'frameBorder:0,src:javascript:""'});
			cj.util.setStyle(ieMask, {
				width :  cj.util.getElmSize(n).w
				,height : cj.util.getElmSize(n).h
				,left : s.left
				,top : s.top
				,zIndex : s.zIndex
				,opacity : 0.1
			});
			n.ieMask = ieMask;
		}
		,disableSelect : function(){
			if(!cj.d.onselectstart) cj.d.onselectstart = function(){return false};
			if(!cj.d.onmousedown) cj.d.onmousedown = function(){ return false};
		}
		,enableSelect : function(){
			if(cj.d.onselectstart) cj.d.onselectstart = null;
			if(cj.d.onmousedown) cj.d.onmousedown = null;
		}
		,countDown : {
			init : function(){
				var t = this;
				t.n = cj.d.getElementById('cjCountDown');
				if(!t.n) return;
				t.n.sec = t.n.getAttribute('sec');
				t.start();
			}
			,start : function(){
				var t = this;
				t.n.sec = Math.max(1, t.n.sec);
				t.n.innerHTML = t.n.sec;
				t.n.sec --;
				setTimeout(function(){cj.util.countDown.start();}, 1000);
			}
		}
		,cssMode : function(){
			return document.compatMode
		}
	}
	,ajax : {
		// {URL:, onComplete:, cb:}
		open : function(set){
			var t = this, req = this.getReq();
			if (!req) return;
			if(set.onStart)	set.onStart();
			method = (set.postData) ? 'POST' : 'GET';
			req.open(method, set.URL, true);
			req.setRequestHeader('User-Agent', 'XMLHTTP');
			if (set.postData) req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
			req.onreadystatechange = function(){
				if(cj.isIE6){
					try{
						if(typeof req.responseText == 'string'){
							setTimeout(function(){
								if(set.onComplete) set.onComplete(req);
								if(set.cb) set.cb(req);
							}, 100);
							req.onreadystateChange = function(){};
						}
					}catch(e){alert('Connection timeout, please try again');}
				}else if(this.readyState === 4 || typeof this.readyState == 'undefined'){
					setTimeout(function(){
						if(set.onComplete) set.onComplete(req);
						if(set.cb) set.cb(req);
					}, 100);
					req.onreadystateChange = function(){};
				}
			}
			if (req.readyState == 4) return;
			req.send(set.postData);
		}
		,getReq : function(){
			var req = null;
			var factories = [
				function() { return new XMLHttpRequest()}
				,function(){ return new ActiveXObject('Msxml2.XMLHTTP')}
				,function(){ return new ActiveXObject('Msxml3.XMLHTTP')}
				,function(){ return new ActiveXObject('Microsoft.XMLHTTP')}
			];
			for (var i=0; i<factories.length; i++){
				try{
					req = factories[i]();
				}catch(e){ continue;}
				break;
			}
			return req;
		}
	}
	,drag : function(n, ev){
		var ev = ev || cj.w.event;
		var t = this, b = cj.d.documentElement || t.d.body, ws, vp, mdp, np, ns, tag, min_dx, max_dx;
		vp = t.util.getVP();
		vp.w -= 2;
		vp.h -= 2;
		ws = t.util.getSize(b);
		ws.w = Math.max(vp.w, ws.w);
		ws.h = Math.max(vp.h, ws.h);
		mdp = t.util.getMousePos(ev);
		np = t.util.getElmPos(n);
		ns = t.util.getSize(n);

		tag = (t.isIE6) ? 'iframe' : 'div';
		min_dx = vp.x - np.x;
		max_dx = vp.x + vp.w - np.x - ns.w;

		if(!t.bodyMask) t.bodyMask = cj.util.addElm(t.d.body, {tag:tag, 'class':'cjBodyMask',style:{opacity:0.5}});
		t.util.setStyle(t.bodyMask, {width:vp.w+'px', height:vp.h+'px', zIndex:parseInt(n.style.zIndex)-100, display:'block'});

		if(!n.cp) n.cp = cj.util.addElm(t.d.body, {tag:tag, 'class':'cjMoveMask', style:{opacity:0.5}});
		t.util.setStyle(n.cp, {width:n.style.width, height:n.style.height, left:n.style.left, top:n.style.top, zIndex:parseInt(n.style.zIndex)+1, display:'block'});

		t.util.disableSelect();
		mu = t.evt.add(cj.d, 'mouseup', function(){
			t.util.enableSelect();
			t.evt.remove(cj.d, 'mouseup', mu);
			t.evt.remove(cj.d, 'mousemove', mm);
			t.util.setStyle(n, {width:n.cp.style.width, height:n.cp.style.height, left:n.cp.style.left, top:n.cp.style.top});
			n.cp.style.display = 'none';
			t.bodyMask.style.display = 'none';
			b.style.overflow = 'auto';
			t.evt.cancel(ev);
		});
		mm = t.evt.add(t.d, 'mousemove', function(ev){
			var dx = dy = 0;
			var ev = ev || cj.w.event;
			var mmp = cj.util.getMousePos(ev);

			dx = mmp.x - mdp.x;
			dy = mmp.y - mdp.y;
			dx = Math.max(dx, vp.x - np.x);
			dx = Math.min(dx, vp.x + vp.w - np.x - ns.w);
			dy = Math.max(dy, vp.y - np.y);
			dy = Math.min(dy, vp.y + vp.h - np.y - ns.h);

			if(dx + dy != 0){
				n.cp.style.left = np.x + dx + 'px';
				n.cp.style.top = np.y + dy + 'px';
			}
			t.evt.cancel(ev);
		});
		t.evt.cancel(ev);
	}
	,fade : {
		fps : 10,
		start : function(n, time, start, end){
			var t = this;
			n.steps = (end - start) / (time * t.fps) ;
			n.timer = null;
			t.dofade(n, start, end);
		}
		,dofade : function (n, current, end){
			var t = this, dir
			dir = (n.steps > 0);
			current += n.steps;
			cj.util.setOpacity(n, current);

			if (dir ^ (current - end > 0)){
				n.timer = setTimeout(function(){ cj.fade.dofade(n, current, end)}, 1000/t.fps);
			}else{
				clearTimeout(n.timer);
				n.timer = null;
			}
		}
	}
	,popMsg : {
		div : null,
		move : 10,
		timer : null,
		holdTime : 3 * 1000,
		init : function(msg, pos, size, holdTime){
			var t = this;
			t.size = size || {w:100, h:20}
			if(holdTime) t.holdTime = holdTime * 1000;
			t.clear();
			t.div = cj.util.addElm(cj.d.body, {tag:'div', 'class':'cjPopMsg', innerHTML:msg, style:{left:pos.x,top:pos.y} });
			this.show();
		}
		,show : function(step){
			var t = this, w, h;
			step = step || 1;
			if(t.div.offsetWidth < t.size.w){
				w = Math.abs((t.size.w/t.move)*step);
				h = Math.abs((t.size.h/t.move)*step);
				cj.util.setStyle(t.div, {width:w,height:h});
				t.timer = setTimeout( function(){ cj.popMsg.show(++step) }, 1 );
			}else{
				t.timer = setTimeout( function(){cj.popMsg.clear()}, t.holdTime);
			}
		}
		,clear : function(){
			if (this.div){
				clearTimeout(this.timer);
				this.timer = null;
				cj.d.body.removeChild(this.div);
				this.div = null;
			}
		}
	}
	,form : {
		chk : function(f, fields){
			if(!f)	return false;
			if(typeof f.lang == 'undefined' || !f.lang){
				alert('lang not set');
				return false;
			}
			var lang = f.lang.value;

			var vp = cj.util.getVP();
			for (var i=0; i<fields.length; i++){
				var a = fields[i].split(',');
				var obj = f[a[0]];
				if(!obj){
					alert(a[0] + ' not set');
					return false;
				}
				var type = a[1];
				var title = obj.getAttribute('title');
				if(!title){
					alert(a[0] + ' title not set');
					return false;
				}
				var pos = cj.util.getElmPos(obj);
				pos.x +=  obj.offsetWidth + 10;
				var size = {w:100,h:30}
				if((pos.x+size.w)>vp.w){
					pos.x = vp.w - size.w;
				}
				var t = 3;
				switch (type){
					case 'num':
						obj.value = cj.form.trim(obj.value);
						if( !cj.form.isNumber(obj.value)){
							obj.focus();
							cj.popMsg.init(title + cj.form.msg.not_number[lang], pos, size, t);
							return false;
						}
					case 'text':
						if( obj.value == '' ){
							obj.focus();
							cj.popMsg.init(title + cj.form.msg.not_null[lang], pos, size, t);
							return false;
						}
					break;
					case 'date':
						if(!cj.form.isDate(obj.value)){
							obj.focus();
							cj.popMsg.init(title + cj.form.msg.not_null[lang], pos, size, t);
							return false;
						}
					break;
					case 'email':
						if(!cj.form.isEmail(obj.value)){
							obj.focus();
							cj.popMsg.init(cj.form.msg.valid[lang] + title, pos, size, t);
							return false;
						}
					break;
					case 'account':
						if(!cj.form.isAccount(obj.value)){
							obj.focus();
							cj.popMsg.init(cj.form.msg.valid[lang] + title, pos, size, t);
							return false;
						}
					break;
					case 'password':
						if(!cj.form.isPasswd(obj.value)){
							obj.focus();
							cj.popMsg.init(cj.form.msg.valid[lang] + title, pos, size, t);
							return false;
						}
						if(obj.getAttribute('confirm')){
							var passwd2 = f[obj.getAttribute('confirm')];
							if(passwd2){
								if(obj.value != passwd2.value){
									passwd2.focus();
									cj.popMsg.init(cj.form.msg.valid[lang] + passwd2.getAttribute('title'), pos, size, t);
									return false;
								}
							}
						}
					break;
					case 'checkbox':
						if(!obj.checked){
							obj.focus();
							cj.popMsg.init(obj.getAttribute('title'),pos, size, t);
							return false;
						}
					break;
					case 'creditCard':
						var cardname = document.getElementById(obj.getAttribute('cardName'));
						if (!cardname){
							alert('Attribute : cardName not set');
							return false;
						}
						if(!cj.form.checkCreditCard.check(cardname.value, obj.value)){
							obj.focus();
							cj.popMsg.init(cj.form.msg.valid[lang] + title, pos, size, t);
							return false;
						}
					break;
					case 'sid':
						if(!cj.form.isSid(obj.value)){
							obj.focus();
							cj.popMsg.init(cj.form.msg.valid[lang] + title, pos, size, t);
							return false;
						}
					break;
				}
			}
			return true;
		},
		isEmail : function(elm){
			return /^([_a-z0-9-]+)(\.[_a-z0-9-]+)*@([a-z0-9-]+)(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/.test(elm);
		},
		isAccount : function(s){
			if(/[^a-z^A-Z^0-9^\.]/.test(s)) return false;
			return /[a-zA-Z0-9\.]{3,30}/.test(s)
		},
		isPasswd : function(s){
			return /.{6,30}/.test(s);
		},
		isNumber : function(obj){
			var exp = /^\d+\.?\d*$/;
			return (exp.exec(obj));
		},
		isSid : function(id){
			code = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29, 0,30,31, 0];
			id = id.toLowerCase();
			if (id.length != 10) return false;
			re = /[a-z]/
			if( !id.charAt(0).match(re) ) return false;
			re = /[0-9]/
			for (i=1; i<10; i++){
				if ( !id.charAt(i).match(re) ){
					return false;
				}
			}
			id0 = code[id.charAt(0).charCodeAt(0)-97];
			if (!id0) return false;
			return !((10-id.charAt(9)-(Math.floor(id0/10) +(id0%10)*9 + id.charAt(1)*8 + id.charAt(2)*7 + id.charAt(3)*6 + id.charAt(4)*5 + id.charAt(5)*4 + id.charAt(6)*3 + id.charAt(7)*2 + id.charAt(8)*1)%10)%10);
		},
		trim : function(obj){
			return obj.replace(/\s/g, '');
		},
		msg : {
			not_null : {
				zh_tw	: ' 必填 ',
				en		: ' is required! '
			},
			valid : {
				zh_tw	: ' 請輸入有效的 ',
				en		: ' Please specify valid '
			},
			day : {
				zh_tw	: '日期',
				en		: 'Date'
			},
			not_number : {
				zh_tw	: ' 不是數字',
				en		: ' is not number'
			}
		},
		isDate : function(d){
			return(/\d{4}[\/-]\d{2}[[\/-]\d{2}/.text(d));
		}
	}
}
cj.flashObj = {
	init : function (set){
		this.src       = set.src;
		this.width     = set.w;
		this.height    = set.h;
		this.version   = '7,0,14,0';
		this.id        = null;
		this.flashVars = null;
		this.params = set.params.split(',') || [];
		return this;
	},
	setVersion : function(v){
		this.version = v;
	},
	setId : function(id){
		this.id = id;
	},
	setBgcolor : function(bgc){
		this.bgcolor = bgc;
	},
	setFlashvars : function(fv){
		this.flashVars = fv;
	},
	toString : function(){
	    var flashTag = new String();
	    if (cj.isIE){
	        flashTag += '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" ';
	        if (this.id != null) flashTag += 'id="'+this.id+'" ';
	        flashTag += 'codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version='+this.version+'" ';
	        flashTag += 'width="'+this.width+'" ';
	        flashTag += 'height="'+this.height+'" />';
	        flashTag += '<param name="movie" value="'+this.src+'" />';
	        flashTag += '<param name="quality" value="high" />';
	        flashTag += '<param name="wmode" value="transparent" />';
	        for(var i=0; i<this.params.length/2; i++) flashTag += '<param name="' + this.params[i*2] + '" value="' + this.params[i*2+1] + '" />';
	        if (this.flashVars != null) flashTag += '<param name="flashvars" value="'+this.flashVars+'" />';
	        flashTag += '</object>';
	    }else{
	    	allowfullscreen="true"
	        flashTag += '<embed src="'+this.src+'" ';
	        if (this.id != null) flashTag += 'name="'+this.id+'" ';
	        flashTag += 'quality="high" wmode="transparent" ';
	        flashTag += 'width="'+this.width+'" ';
	        flashTag += 'height="'+this.height+'" ';
	        flashTag += 'type="application/x-shockwave-flash" ';
	        for(var i=0; i<this.params.length/2; i++) flashTag += this.params[i*2] + '="' + this.params[i*2+1] + '" ';
	        if (this.flashVars != null) flashTag += 'flashvars="'+this.flashVars+'" ';
	        flashTag += 'pluginspage="http://www.macromedia.com/go/getflashplayer">';
	        flashTag += '</embed>';
	    }
	    return flashTag;
	},
	write : function(set){
		if(set) this.init(set);
    	cj.d.write(this.toString());
    }
}