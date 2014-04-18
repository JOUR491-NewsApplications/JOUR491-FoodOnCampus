#!/usr/bin/env python
# encoding: utf-8

import os, sys, string, xml, urllib2, time

from dateutil import parser

from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings") 

from django.template.defaultfilters import slugify, urlize

from menu.models import Hall, Meal, FoodType, Food, Menu

#hallresponse = urllib2.urlopen('http://menu.unl.edu/services/dailymenu.aspx?action=getcomplexes')

#hallsoup = BeautifulSoup(hallresponse, "xml")

#for hall in hallsoup.find_all('getcomplexes'):
#    cid = hall.ComplexId.string
#    hallname = hall.ComplexName.string
#    hall_slug = slugify(hallname)
#    x = hall.Latitude.string
#    y = hall.Longitude.string
#    resid, residcreated = Hall.objects.get_or_create(name=hallname, name_slug=hall_slug, location_x=x, location_y=y, complex_id=cid)
#    print "Created %s" % resid

halls = Hall.objects.all()

for hall in halls:
    hallcall = int(hall.complex_id)
    url = "http://menu.unl.edu/services/dailymenu.aspx?action=getdailymenuforentireday&complexId=%i&mealdate=04-16-2014" % hallcall
    menuresponse = urllib2.urlopen(url)
    menusoup = BeautifulSoup(menuresponse, "xml")
    for item in menusoup.find_all('getdailymenuforentireday'):
        #first we get or create a meal
        mealname = item.MealName.string
        mealnameslug = slugify(item.MealName.string)
        m, mcreated = Meal.objects.get_or_create(name=mealname, name_slug=mealnameslug)
        #next we get or create the food types
        #ftype = item.TrimedCourseName.string
        #ftype_slug = slugify(ftype)
        #fudtype, fudtypecreated = FoodType.objects.get_or_create(name=ftype, name_slug=ftype_slug)
        #now we create the food
        #fudname = item.MealItemName.string
        #fudnameslug = slugify(fudname)
        #fud, fudcreated = Food.objects.get_or_create(name=fudname, name_slug=fudnameslug, food_type=fudtype)
        #now we assemble our menu for the day
        #mdate = parser.parse(item.MealDate.string)
        #mstart = parser.parse(item.MealStartDateTime.string)
        #mend = parser.parse(item.MealEndDateTime.string)
        #try:
        #     chowtime = Menu.objects.get(date=mdate, meal_start=mstart, meal_end=mend, meal=meel, hall=hall)
        #     chowtime.food.add(fud)
        #     print "Added %s" % fud
        #except:
        #     chowtime, chowtimecreated = Menu.objects.get(date=mdate, meal_start=mstart, meal_end=mend, meal=meel, hall=hall, food=fud)
        #     print "Created %s" % chowtime
        time.sleep(1)
    
    

