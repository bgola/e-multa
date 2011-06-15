# coding: utf-8

from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET

@require_GET
def home(request):

    return render_to_response("home.html")
