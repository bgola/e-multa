function toggleinfo() {
	this.openInfoWindow();
};

$('div.gmap:visible').css('width', '100%');
$('div.gmap:visible').css('height', '100%');
$('div.gmap:visible *').css('width', '100%');
$('div.gmap:visible *').css('height', '100%');

if (window.attachEvent) { 
	window.attachEvent("onresize", function() { $('div.gmap:visible').getMap().onResize()} );
} else {
	window.addEventListener("resize", function() {$('div.gmap:visible').getMap().onResize()} , false);
}

