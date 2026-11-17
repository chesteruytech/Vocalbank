from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import VOCALOID, Producer

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

def producers(request):
    if request.method == "POST":
        Producer.objects.create(
            name=request.POST.get('name'),
            alias=request.POST.get('alias') or None,
            country=request.POST.get('country'),
            debutyear=request.POST.get('debutyear'),
            isactive=request.POST.get('isactive') == 'on',
        )
        return redirect('producers')

    queryset = Producer.objects.all().order_by('producerid')
    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', '')
    if search:
        if search.isdigit():
            queryset = queryset.filter(Q(producerid=int(search)) | Q(name__icontains=search))
        else:
            queryset = queryset.filter(name__icontains=search)
    if status == 'active':
        queryset = queryset.filter(isactive=True)
    elif status == 'inactive':
        queryset = queryset.filter(isactive=False)

    return render(request, 'app/producers.html',
                  {'producers': queryset, 'search': search, 'status': status})


def update_producer(request, producerid):
    producer = get_object_or_404(Producer, pk=producerid)
    if request.method == "POST":
        producer.name = request.POST.get('name')
        producer.alias = request.POST.get('alias') or None
        producer.country = request.POST.get('country')
        producer.debutyear = request.POST.get('debutyear')
        producer.isactive = request.POST.get('isactive') == 'on'
        producer.save()
        return redirect('producers')
    return render(request, 'app/producer_form.html', {'producer': producer})


def delete_producer(request, producerid):
    producer = get_object_or_404(Producer, pk=producerid)
    if request.method == "POST":
        try:
            producer.delete()
        except IntegrityError:
            messages.error(request, "Can't delete: this producer still has songs.")
    return redirect('producers')


def producer_activity_report(request):
    rows = None
    year = request.GET.get('year')
    month = request.GET.get('month')
    if year and month:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.producerid, p.name, p.isactive, COUNT(s.songid) AS songs_released
                FROM producer p
                JOIN song s ON s.producerid = p.producerid
                WHERE YEAR(s.releasedate) = %s AND MONTH(s.releasedate) = %s
                GROUP BY p.producerid, p.name, p.isactive
                ORDER BY songs_released DESC
            """, [year, month])
            rows = cursor.fetchall()
    return render(request, 'app/producer_report.html',
                  {'rows': rows, 'year': year, 'month': month})