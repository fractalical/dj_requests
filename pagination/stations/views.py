import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))

    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        reader = [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']} for row in reader]

    paginator = Paginator(reader, 10)
    page = paginator.page(page_number)

    context = {
        'bus_stations': paginator,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
