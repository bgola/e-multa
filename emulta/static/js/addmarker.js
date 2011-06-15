var marker = null;
function addmarker(e) {
	var map = $('div.gmap:visible');
	if (!marker) {
		marker = new google.maps.Marker({position: e.latLng, map: map.getMap()});
	} 
	marker.setPosition(e.latLng);
	$('#id_location').val(e.latLng);
}
