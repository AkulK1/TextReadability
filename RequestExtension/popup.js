document.getElementById( "infoButton" ).onclick = function(){
	console.log( "info button pressed" );
	getAnswer( true );
}
document.getElementById( "fictionButton" ).onclick = function(){
	console.log( "fiction button pressed" );
	getAnswer(false);
}

function getAnswer( isInfo ){

	
	var loadScreen  = document.getElementById( "loadingScreen" );
	loadScreen.className = "loader";
	var query = { active: true, currentWindow: true };
	document.body.style.width = "500px";
	document.getElementById( "textdifficulty" ).innerHTML = "";
	document.getElementById( "worddefs" ).innerHTML = "";
	
	chrome.tabs.query( query, function( tabs ){
		
		var currentTab = tabs[0];
		let Url = currentTab.url;
		var xhr = new XMLHttpRequest();
		xhr.open( "POST", "https://ds-text-readability-20.herokuapp.com/fullpredict" );
		xhr.setRequestHeader('Content-Type', 'application/json');
		var category = -1;
		if( isInfo ){
			category = 1;
		} else {
			category = 0;
		}
		
		xhr.send( JSON.stringify({
			article_url: String(Url), info: category
		}));
		
		xhr.onreadystatechange = function(){
			if (this.readyState == 4 && this.status == 200){
				loadScreen.className = "";
				var responseJSON = JSON.parse( xhr.responseText );
				var tdiff = responseJSON.response;
				var gradeLevel = "Sorry. URL not compatible. Try copy and pasting text at our <a href ='http://lexlearntogether.com/'> website </a>";
				if( tdiff == 1 ){
					gradeLevel = "Kindergarten";
				} else if( tdiff == 2 ){
					gradeLevel = "First to Second Grade";
				} else if( tdiff == 3 ){
					gradeLevel = "Third to Fourth Grade";
				} else if( tdiff == 4 ){
					gradeLevel = "Fifth to Sixth Grade";
				} else if( tdiff == 5 ){
					gradeLevel = "Seventh to Eighth Grade";
				} else if( tdiff == 6 ){
						gradeLevel = "High School Level or Above";
				}
				
				document.getElementById( "textdifficulty" ).innerHTML = "<b>Difficulty</b>" + ": "+ gradeLevel;
				htmlList = document.getElementById( "worddefs" );
				for( var propt in responseJSON.diff_words ){
					var cur_li = document.createElement( "li" );
					var temp_str =  propt.bold()  + ": " + responseJSON.diff_words[propt];
					cur_li.innerHTML =  temp_str ;
					htmlList.appendChild( cur_li );
				}
				
			}
			
		}
	});
}
