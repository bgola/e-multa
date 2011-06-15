# coding: utf-8

from django.forms import ModelForm, Field, Form
from django.forms.widgets import HiddenInput, SplitHiddenDateTimeWidget
from django.forms.fields import DateTimeField
from django.contrib.admin import widgets

from gmapi.forms.widgets import GoogleMap
from datetime import datetime

from models import Offence


class OffenceForm(ModelForm):
    map = Field(label='Local', required=False, widget=GoogleMap(attrs={'width':510, 'height':510}))

    class Meta:
        model = Offence
        widgets = {
                    'location': HiddenInput(),
                }

    class Media:
        js = ['js/jquery-ui-1.8.13.custom/js/jquery-ui-1.8.13.custom.min.js',
              'js/jquery.maskedinput-1.3.min.js',
              'js/timepicker.js',
              'js/offenceform.js']

        css = {'all': ["css/ui-lightness/jquery-ui-1.7.2.custom.css"]}

class MapForm(Form):
    map = Field(label="", required=False, widget=GoogleMap(attrs={'width':800, 'height':600}))
    class Media:
        js = ['js/infowindow.js']
