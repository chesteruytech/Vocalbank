from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def maintenance(request):
    return HttpResponse("This is a CCINFOM project. Vocalbank DB Application Project under maintenance.")