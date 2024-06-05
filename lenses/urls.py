from django.conf.urls import url

from . import views

app_name = 'lenses'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^table/$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^links/$', views.links, name='links'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^(?P<globject_id>[0-9]+)/$', views.detail, name='detail'),
]

"""
URL patterns for the 'lenses' app.

This module defines the URL patterns for the 'lenses' app in the Django project.
Each URL pattern is associated with a specific view function that handles the request.

- The 'main' view function is associated with the root URL ('/').
- The 'index' view function is associated with the '/table/' URL.
- The 'search' view function is associated with the '/search/' URL.
- The 'links' view function is associated with the '/links/' URL.
- The 'contacts' view function is associated with the '/contacts/' URL.
- The 'detail' view function is associated with URLs that match the pattern '/<globject_id>/'.

The 'name' parameter in each URL pattern is used to provide a unique identifier for the URL,
which can be used to reverse-resolve the URL in the Django templates.

For more information on URL patterns in Django, refer to the Django documentation.
"""
