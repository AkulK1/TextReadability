x = document.createElement("BUTTON");
t = document.createTextNode("Click here if it's info text");
x.appendChild(t);
document.body.appendChild(x);

var y = document.createElement("BUTTON");
var z = document.createTextNode("Click here if it's an English Language text");
y.appendChild(z);
document.body.appendChild(y);

x.onclick = function(){
	getAnswer( true );
}


y.onclick = function(){
	getAnswer( false );
}
/*function() {
    var query = { active: true, currentWindow: true };
	function callback(tabs) {
  	var currentTab = tabs[0]; 
  	chrome.runtime.sendMessage( {clicked: true, curTab: currentTab, info: false}, function( response ){
	  	document.getElementById( "textdifficulty" ).innerHTML = response.res;
  		});
	}
	chrome.tabs.query(query, callback);
}	*/


function getAnswer( isInfo ){
	var query = { active: true, currentWindow: true };
	function callback(tabs) {
		document.getElementById( "textdifficulty" ).innerHTML = "Loading";
		var currentTab = tabs[0]; 
		chrome.runtime.sendMessage( {clicked: true, curTab: currentTab, info: Boolean(isInfo)}, function( response ){
			document.body.style.width = "500px";
			var responseJSON = JSON.parse( response.res );
			var tdiff = responseJSON.response;
			document.getElementById( "textdifficulty" ).innerHTML = tdiff;
			
			htmlList = document.getElementById( "worddefs" );
			console.log( responseJSON.diff_words );
			for( var propt in responseJSON.diff_words ){
				var cur_li = document.createElement( "li" );
				var temp_str =  propt.bold()  + ": " + responseJSON.diff_words[propt];
				cur_li.innerHTML =  temp_str ;
				htmlList.appendChild( cur_li );
				
			}
			
  		});
	}
	chrome.tabs.query(query, callback);
}
