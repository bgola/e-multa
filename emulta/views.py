# coding: utf-8

from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET
from django.template import RequestContext

from gmapi import maps

from offence.forms import OffenceForm

@require_GET
def home(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(-23, -46),
        'mapTypeId': maps.MapTypeId.HYBRID,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },

    })
    maps.event.addListener(gmap, 'click', 'addmarker')
    form = OffenceForm(initial={'map': gmap})
    return render_to_response("home.html", {'form': form}, 
                            context_instance=RequestContext(request))
