chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked( tab ){
	console.log('background running');
	var xhr = new XMLHttpRequest();
	xhr.open( "POST", "https://ds-text-readability-20.herokuapp.com/urlpred" );
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
			alert ( xhr.responseText );
		}
	}
	console.log( tab );
}
