x = document.createElement("BUTTON");
t = document.createTextNode("Click here if it's info text");
x.appendChild(t);
document.body.appendChild(x);

var y = document.createElement("BUTTON");
var z = document.createTextNode("Click here if it's an English Language text");
y.appendChild(z);
document.body.appendChild(y);

x.onclick = function() {
    var query = { active: true, currentWindow: true };
	function callback(tabs) {
  	var currentTab = tabs[0]; 
  	chrome.runtime.sendMessage( {clicked: true, curTab: currentTab, info: true}, function( response ){
	  	document.getElementById( "textdifficulty" ).innerHTML = response.res;
  		});
	}
	chrome.tabs.query(query, callback);
}	

y.onclick = function() {
    var query = { active: true, currentWindow: true };
	function callback(tabs) {
  	var currentTab = tabs[0]; 
  	chrome.runtime.sendMessage( {clicked: true, curTab: currentTab, info: false}, function( response ){
	  	document.getElementById( "textdifficulty" ).innerHTML = response.res;
  		});
	}
	chrome.tabs.query(query, callback);
}	
