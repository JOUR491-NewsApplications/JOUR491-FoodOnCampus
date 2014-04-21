from django.shortcuts import render
from django.db.models import Count
from menu.models import Hall, Menu
import datetime

#now = datetime.datetime.now()
now = datetime.datetime(2014, 4, 18)

#For later
#q = Menu.objects.annotate(Count('food')).order_by('-food__count')


def home(request):
    halls=Hall.objects.order_by('name')
    return render(request, 'index.html', {'halls': halls})

def halldetail(request, slug):
    hall=Hall.objects.get(name_slug=slug)
    menus=Menu.objects.filter(hall=hall, date=now)
    return render(request, 'halldetail.html', {'hall': hall, 'menus': menus})
