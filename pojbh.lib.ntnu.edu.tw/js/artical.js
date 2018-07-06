cj.init({require:'simpleMenu,roller,inline_popup'});

var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
cj.util.loadJs(gaJsHost + "google-analytics.com/ga.js");
cj.evt.add(cj.w, 'load', function(){
	try {
		var pageTracker = _gat._getTracker("UA-10994216-1");
		pageTracker._trackPageview();
	}catch(err){}
});

cj.fn = {
	sortby : function(v){
		var f = document.getElementById('artical_search');
		f.order.value = v;
		f.submit();
	},
	showContent : {
		c : null,
		tailo : null,
		lang : null,
		obj : null,
		init : function(){
			var c = document.getElementById('artical_content');
			var tailo = document.getElementById('artical_tailo');
			if(c&&tailo){
				this.obj = c;
				this.c = c.innerHTML;
				this.tailo = tailo.innerHTML;
				this.btn1 = document.getElementById('showContentBtn1');
				this.btn2 = document.getElementById('showContentBtn2');
				this.btn3 = document.getElementById('showContentBtn3');
			}

		},
		show : function(lang){
			if(this.c&&this.tailo){
				switch(lang){
					default:
						this.obj.innerHTML = this.c;
						this.btn1.className = 'sc-on'
						this.btn2.className = 'sc-off'
						this.btn3.className = 'sc-off'
						break;
					case 'tailo':
						this.obj.innerHTML = this.tailo;
						this.btn1.className = 'sc-off'
						this.btn2.className = 'sc-on'
						this.btn3.className = 'sc-off'
						break;
					case 'all':
						this.obj.innerHTML = "<div style='width:48%; border:1px solid #ccc; float:left; padding:3px;'>"+this.c+"</div><div style='width:48%;border:1px solid #ccc; float:left;margin-left:5px; padding:3px;'>" + this.tailo + "</div>";
						this.btn1.className = 'sc-off'
						this.btn2.className = 'sc-off'
						this.btn3.className = 'sc-on'
						break;
				}
			}
		}
	}
	,closePopup : function(){
		try{
			var w = cj.w.parent;
			if(cj.w.name == 'popup'){
				w.focus();
				cj.w.close();
			}else{
				w.cj.inline_popup.close();
			}
		}catch(e){}
	}}
cj.evt.add(window, 'load', function(){
	this.focus();

	//fix mainContent height
	var mc = cj.d.getElementById('mainContent');
	if(mc){
		var vp = cj.util.getVP();
		mc.style.height = Math.max(mc.offsetHeight, vp.h-460) + 'px';
	}

	cj.simpleMenu.init(['cjNavMenu2','cjNavMenu3','cjNavMenu4','cjNavMenu5'], ['cjNavItem2', 'cjNavItem3', 'cjNavItem4', 'cjNavItem5']);
	cj.fn.showContent.init();

	var f = document.getElementById('artical_full_search');
	if (f){
		if(!f.keyword) return;
		var k_default = f.keyword.getAttribute('default');
		var k_msg = f.keyword.getAttribute('msg');
		f.keyword.onfocus = function(){
			if (this.value==k_default){
				this.value = '';
			}
		};
		f.onsubmit = function(){
			/*
			if( (f.keyword.value==k_default || f.keyword.value=='') && f.a_period.selectedIndex==0 && f.a_ctype_id.selectedIndex==0 && f.a_author_id.selectedIndex==0){
				f.keyword.focus();
				var pos = cj.util.getElementPos(f.keyword);
				pos.top += f.keyword.offsetHeight + 5;
				cj.util.popMsg.init(k_msg, pos, {"width":200, "height":20});
				return false;
			}
			*/

			if (this.keyword.value==k_default){
				this.keyword.value = '';
			}
			var url = 'artical-d';
			if(f.a_period&&f.a_period.selectedIndex){
				url += f.a_period.value;
			}
			url += 't';
			if(f.a_ctype_id&&f.a_ctype_id.selectedIndex){

				url += f.a_ctype_id.value;
			}
			url += 'a';
			if(f.a_author_id&&f.a_author_id.selectedIndex){
				url += f.a_author_id.value;
			}
			url += 'p.htm';
			this.action=url;

			this.submit();
		}
	}

	var floater = document.getElementById("floater");
	var Base = document.getElementById("Base");
	if (floater && Base){
		var top = 0;
		var left = 0;
		function setFloaterPos(){
			floater.pos = cj.util.getElementPos(Base);
			floater.style.left = floater.pos.left + left + "px";
			floater.style.top = floater.pos.top + top + cj.util.getScrollPos().top + "px";
		}
		setFloaterPos();
		cj.evt.add(window, "scroll", function(){setFloaterPos()});
		cj.evt.add(window, "resize", function(){setFloaterPos()});
	}
	
	var ipts = document.getElementsByTagName('input');
	for(var i=0; i<ipts.length; i++){
		n = ipts[i];
		if(/inpPage/.test(n.id)){
			if(!cj.goToPage){
				cj.goToPage = {
					url :  n.getAttribute('url')
					,max: n.getAttribute('max')
					,v : parseInt(n.value) - 1
				};
			}
			n.onkeyup = function(){
				cj.goToPage.v = parseInt(this.value) - 1;
				cj.d.getElementById('debug').value = cj.goToPage.v;
			}
		}
	}
	
	var as = document.getElementsByTagName('a');
	for(var i=0; i<as.length; i++){
		n = as[i];
		if(/chgPage/.test(n.id)){
			n.onclick = function(){
				if(cj.goToPage.v>=0 && cj.goToPage.v<cj.goToPage.max){
					url = cj.goToPage.url + cj.goToPage.v + '.htm';
					window.location = url;
				}else{
					alert('Out of range!');
				}
				return false;
			}
		}
	}
	
	/*
	var chgPage = document.getElementById('chgPage');
	var inpPage = document.getElementById('inpPage');
	if(chgPage && inpPage){
		chgPage.onclick = function(){
			var ua = inpPage.getAttribute('url');
			var np = inpPage.value -1;
			var max = inpPage.getAttribute('max') -1;
			if( cj.form.isNumber(inpPage.value)){
				ua += Math.min(max, Math.max(0, np)) + '.htm';
				window.location = ua;
			}else{
				inpPage.value='1';
				alert('Outof range');
				return false;
			}
		}
	}
	*/
});