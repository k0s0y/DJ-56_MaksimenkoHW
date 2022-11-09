from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv

bus_station_list = []
with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        bus_station_dict = {}
        bus_station_dict['Name'] = row['Name']
        bus_station_dict['Street'] = row['Street']
        bus_station_dict['District'] = row['District']
        bus_station_list.append(bus_station_dict)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_station_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,

    }
    return render(request, 'stations/index.html', context)
