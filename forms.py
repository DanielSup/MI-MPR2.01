from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.validators import FileExtensionValidator

from django import forms

class MyForm(forms.Form):
    field = forms.FileField(label='Upload video', validators=[FileExtensionValidator(allowed_extensions=["mp4", "avi", "flv"])])
    action = forms.ChoiceField(choices=[('watch', 'Watch the video with speeds of the vehicles'),
                                        ('annotate', 'Watch the video with speed of the vehicles and annotations'),
                                         ('download', 'Download video with speeds of the vehicles')], widget=forms.RadioSelect, label='')