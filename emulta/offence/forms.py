# coding: utf-8

from django.forms import ModelForm, Field, Form
from django.forms.widgets import HiddenInput
from gmapi.forms.widgets import GoogleMap

from models import Offence

class OffenceForm(ModelForm):
    map = Field(label='Local', required=False, widget=GoogleMap(attrs={'width':510, 'height':510}))

    class Meta:
        model = Offence
        widgets = {
                    'location': HiddenInput(),
                }

    class Media:
        js = ['js/addmarker.js']

class MapForm(Form):
    map = Field(label="", required=False, widget=GoogleMap(attrs={'width':800, 'height':600}))
    class Media:
        js = ['js/infowindow.js']


