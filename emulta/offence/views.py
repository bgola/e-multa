# coding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.template import RequestContext, Template, Context

from gmapi import maps

from forms import OffenceForm, MapForm
from models import Offence

@require_POST
def submit(request):
    form = OffenceForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/offence/view/')
    return render_to_response("home.html", {'form': form}, 
                            context_instance=RequestContext(request))

@require_GET
def view(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(-23, -46),
        'mapTypeId': maps.MapTypeId.HYBRID,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })

    for o in Offence.objects.all():
        ll = o.location[1:-1].split(',')
        position = maps.LatLng(*ll)
        marker = maps.Marker(opts={'map': gmap, 'position': position})
        maps.event.addListener(marker, 'click', 'toggleinfo')
        tmpl = Template("""{% load oembed_tags %}<div>
                  {% oembed %}{{ o.media_url }}{% endoembed %}</div>""")
        iw = maps.InfoWindow(opts={'content': tmpl.render(Context({'o': o}))})
        iw.open(gmap, marker)
    fmap = MapForm(initial={'map': gmap})
    return render_to_response("view.html", {'fmap': fmap}, 
                            context_instance=RequestContext(request))

