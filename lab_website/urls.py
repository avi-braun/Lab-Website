'''This package has the url encodings for the main app.'''

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab_website.views.home', name='home'),
    # url(r'^lab_website/', include('lab_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^communication/', include('communication.urls')), 
    url(r'^papers/', include('papers.urls')),     
)
