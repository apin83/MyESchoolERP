from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def faculty_home(request):
    template = loader.get_template('faculty_home.html')
    return HttpResponse(template.render(request=request))