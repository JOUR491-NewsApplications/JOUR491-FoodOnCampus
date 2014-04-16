#!/usr/bin/env python
# encoding: utf-8

import os, sys, string, xml, urllib2, time

from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings") 

from django.template.defaultfilters import slugify, urlize

from menu.models import Hall, FoodType, Food

#hallresponse = urllib2.urlopen('http://menu.unl.edu/services/dailymenu.aspx?action=getcomplexes')

#hallsoup = BeautifulSoup(hallresponse, "xml")

#for hall in hallsoup.find_all('getcomplexes'):
#    cid = hall.ComplexId.string
#    hallname = hall.ComplexName.string
#    hall_slug = slugify(hallname)
#    x = hall.Latitude.string
#    y = hall.Longitude.string
#    resid, residcreated = Hall.objects.get_or_create(name=hallname, name_slug=hall_slug, location_x=x, location_y=y, complex_id=cid)
#    print residcreated

halllist = Hall.objects.all()

for hallid in halllist:
    hallcall = int(hallid.complex_id)
    url = "http://menu.unl.edu/services/dailymenu.aspx?action=getdailymenuforentireday&complexId=%i&mealdate=04-16-2014&Type=hierarchical" % hallcall
    menuresponse = urllib2.urlopen(url)
    menusoup = BeautifulSoup(menuresponse, "xml")
    for mcourse in menusoup.find_all('MealCourse'):
        ftype_slug = slugify(mcourse['value'])
        ftype, ftypecreated = FoodType.objects.get_or_create(name=mcourse['value'], name_slug=ftype_slug)
        fname = mcourse.FoodItem.MealItem.string
        fname_slug = slugify(fname)
        fud, fudcreated = Food.objects.get_or_create(name=fname, name_slug=fname_slug, food_type=ftype)
        print fname
    time.sleep(2)
    
    

