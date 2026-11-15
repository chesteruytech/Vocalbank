from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import VOCALOID

# Create your views here.
def maintenance(request):
    return HttpResponse("This is a CCINFOM project. Vocalbank DB Application Project under maintenance.")

def vocaloid(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        company = data.get('company')
        language = data.get('language')
        release_date = data.get('releaseDate')
        gender = data.get('gender')

        VOCALOID.objects.create(name=name, company=company, language=language, release_date=release_date, gender=gender)
        return redirect('/')

    queryset = VOCALOID.objects.all()
    if request.GET.get('Search'):
        queryset = queryset.filter(name__icontains=request.GET.get('Search'))

    context = {'vocaloid': queryset}
    return render(request, context) # TODO: Add second parameter for template name between request and context

def update_vocaloid(request):
    gu_vocaloid = get_object_or_404(VOCALOID, id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        company = data.get('company')
        language = data.get('language')
        release_date = data.get('releaseDate')
        gender = data.get('gender')

        gu_vocaloid.name = name
        gu_vocaloid.company = company
        gu_vocaloid.language = language
        gu_vocaloid.release_date = release_date
        gu_vocaloid.gender = gender
        gu_vocaloid.save()
        return redirect('/')

    context = {'vocaloid': gu_vocaloid}
    return render(request, context) # TODO: Add second parameter for template name between request and context

def delete_vocaloid(request):
    gd_vocaloid = get_object_or_404(VOCALOID, id=id)
    gd_vocaloid.delete()
    return redirect('/')