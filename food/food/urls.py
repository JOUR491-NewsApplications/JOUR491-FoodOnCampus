from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'menu.views.home', name='home'),
    url(r'^hall/(?P<slug>[-\w]+)/$', 'menu.views.halldetail', name='halldetail'),
    url(r'^admin/', include(admin.site.urls)),
)
