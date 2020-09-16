console.log ('working')
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
    alert ( xhr.responseText );
  }
}
