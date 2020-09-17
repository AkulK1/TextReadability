console.log( "message sending" );

var query = { active: true, currentWindow: true };
function callback(tabs) {
  var currentTab = tabs[0]; 
  chrome.runtime.sendMessage( {clicked: true, curTab: currentTab}, function( response ){
	  document.getElementById( "textdifficulty" ).innerHTML = response.res;
  });
}
chrome.tabs.query(query, callback);