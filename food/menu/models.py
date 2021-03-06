from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    complex_id = models.IntegerField()
    def get_absolute_url(self):
        return "http://127.0.0.1:8000/hall/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/meal/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class FoodType(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/food-type/%s/" % self.name_slug
    def __unicode__(self):
        return self.name
        
class Food(models.Model):  
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    food_type = models.ForeignKey(FoodType)
    def get_absolute_url(self):
        return "/food/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Menu(models.Model):
    date = models.DateField()
    meal_start = models.DateTimeField()
    meal_end = models.DateTimeField()
    meal = models.ForeignKey(Meal)
    hall = models.ForeignKey(Hall)
    food = models.ManyToManyField(Food, blank=True, null=True)
    def get_absolute_url(self):
        return "/menu/%i/" % self.id
    def __unicode__(self):
        return "Menu for %s" % self.date
