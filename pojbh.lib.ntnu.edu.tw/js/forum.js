cj.evt.add(cj.w, 'load', function(){
	//mbLoginBtn
	var mbLoginBtn = cj.d.getElementById('mbLoginBtn');
	if(mbLoginBtn){
		cj.evt.add(mbLoginBtn, 'click', function(){
			cj.inline_popup.open(mbLoginBtn, {url:'ajax.php?act=mbLoginForm', w:1, h:1});
		});
	}
	//mbJoinBtn
	var mbJoinBtn = cj.d.getElementById('mbJoinBtn');
	if(mbJoinBtn){
		cj.evt.add(mbJoinBtn, 'click', function(){
			cj.inline_popup.open(mbJoinBtn, {url:'ajax.php?act=mbJoinForm', w:1, h:1});
		});
	}
	//logout
	var mbLogoutBtn = cj.d.getElementById('mbLogoutBtn');
	if(mbLogoutBtn){
		cj.evt.add(mbLogoutBtn, 'click', function(){
			cj.inline_popup.open(mbLogoutBtn, {url:'ajax.php?act=logout', w:1, h:1});
		});
	}
	//forumAddBtn
	var forumAddBtn = cj.d.getElementById('forumAddBtn');
	if(forumAddBtn){
		cj.evt.add(forumAddBtn, 'click', function(){
			var mb = forumAddBtn.getAttribute('mb');
			if(mb){
				var vp = cj.util.getVP();
				var w = Math.min(Math.ceil(vp.w*0.8), 100);
				cj.inline_popup.open(forumAddBtn, {url:'ajax.php?act=forumAddForm', w:1, h:1});
			}else{
				alert('請先登入會員');
			}
		});
	}
	//forumReplyBtn
	var forumReplyBtn = cj.d.getElementById('forumReplyBtn');
	if(forumReplyBtn){
		cj.evt.add(forumReplyBtn, 'click', function(){
			var mb = forumReplyBtn.getAttribute('mb');
			var fid = forumReplyBtn.getAttribute('fid');
			if(mb){
				var vp = cj.util.getVP();
				var w = Math.min(Math.ceil(vp.w*0.8), 100);
				cj.inline_popup.open(forumReplyBtn, {url:'ajax.php?act=forumReplyForm&fid='+fid, w:1, h:1});
			}else{
				alert('請先登入會員');
			}
		});
	}

	//blogReplyBtn
	var blogReplyBtn = cj.d.getElementById('blogReplyBtn');
	if(blogReplyBtn){
		blogReplyBtn.onclick = function(){
			var vp = cj.util.getVP();
			//var w = Math.min(Math.ceil(vp.w*0.8), 800);
			cj.inline_popup.open(blogReplyBtn, {url:'ajax.php?act=blogReplyForm', w:1, h:1});
			return false;
		}
	}
});