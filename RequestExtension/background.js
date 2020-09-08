chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked( tab ){
	console.log('background running');
/*	var features = [2.0252650889409836, 0.9944359579571609, -2.232157387088793, -1.8162556390409161, 1.4739928148134387, 2.075016811546231, 1.5365720152313331, 1.0139025870199658, 1.6781185780750947, 1.2940818114033639, 0.39464220890044394, 0.9082579689879631, 1.8060812518375358, 1.0]
	var xhr = new XMLHttpRequest();
	xhr.open( "POST", "https://ds-text-readability-20.herokuapp.com/predict" );
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send( JSON.stringify({
		"input": features
	}));
	
	xhr.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			console.log( xhr.responseText );
		}
	}*/
	console.log( tab );
		
}