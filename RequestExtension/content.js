console.log( "Purple Paragraphs" );

let paras = document.getElementsByTagName( 'p' );
for( var i = 0; i < paras.length; i++ ){
	paras[i].style['background-color'] = '#F0C';
}