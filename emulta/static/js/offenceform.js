var marker = null;
function addmarker(e) {
	var map = $('div.gmap:visible');
	if (!marker) {
		marker = new google.maps.Marker({position: e.latLng, map: map.getMap()});
	} 
	marker.setPosition(e.latLng);
	$('#id_location').val(e.latLng);
}

$('body').ready(function() { 
	$('li.input').each(function() {
		var li = this;
		$('input', li).focus(function() { 
			$('span', li).show();
		});
		$('input', li).blur(function() { 
			$('span', li).hide();
		});

	});
	$('#id_license_plate').mask('aaa-9999');
	$('#id_timestamp').datepicker({
      				duration: '',
        			showTime: true,
        			constrainInput: false,
        			time24h: true
     	});

})


