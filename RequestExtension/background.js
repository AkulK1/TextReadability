chrome.runtime.onMessage.addListener( function (message, sender, sendResponse) {
	if (message.clicked) {
		console.log('background running');
		var xhr = new XMLHttpRequest();
		xhr.open( "POST", "https://ds-text-readability-20.herokuapp.com/fullpredict" );
		xhr.setRequestHeader('Content-Type', 'application/json');
		
		let url = message.curTab.url;
		
		console.log (String(url));
		xhr.send( JSON.stringify({
			article_url: String(url), info: 0
		}));
		

		xhr.onreadystatechange = function(){
			if (this.readyState == 4 && this.status == 200){
				sendResponse( {res: xhr.responseText } );
			}
		}
	}
	return true;
});
/*
function buttonClicked( tab ){
		console.log('background running');
		var xhr = new XMLHttpRequest();
		xhr.open( "POST", "https://ds-text-readability-20.herokuapp.com/fullpredict" );
		xhr.setRequestHeader('Content-Type', 'application/json');
		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let url = tabs[0].url;
			console.log (String(url))
			xhr.send( JSON.stringify({
			article_url: String(url), info: 0
			}));
		});


		xhr.onreadystatechange = function(){
			if (this.readyState == 4 && this.status == 200){
				console.log( xhr.responseText );
				console.log( tab.id );
				var number  = tab.id;
				//chrome.storage.sync.set( {tab.id: xhr.responseText}, function(){} );
				chrome.storage.local.set( {number: xhr.responseText}, function(){});
			}
		}
		console.log( tab );
}*/
