# coding: utf-8

from django.http import HttpResponse 
from django.views.decorators.http import require_GET

@require_GET
def home(request):
    return HttpResponse("Hello, Gondor")
