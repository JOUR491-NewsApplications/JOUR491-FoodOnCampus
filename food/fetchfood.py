#!/usr/bin/env python
# encoding: utf-8

import os, sys, string, xml, urllib2

from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings") 

from django.template.defaultfilters import slugify, urlize

from menu.models import Hall

response = urllib2.urlopen('http://menu.unl.edu/services/dailymenu.aspx?action=getcomplexes')

soup = BeautifulSoup(response, "xml")

for hall in soup.find_all('getcomplexes'):
    cid = hall.ComplexId.string
    hallname = hall.ComplexName.string
    hall_slug = slugify(hallname)
    x = hall.Latitude.string
    y = hall.Longitude.string
    resid, residcreated = Hall.objects.get_or_create(name=hallname, name_slug=hall_slug, location_x=x, location_y=y, complex_id=cid)
    print residcreated



