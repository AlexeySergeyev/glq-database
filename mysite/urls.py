"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.shortcuts import redirect

urlpatterns = [
	# url(r'^lenses/', include('lenses.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^$', lambda request: redirect('lenses/'), name='root-redirect'),  # Redirect root to /lenses
    url(r'^lenses/', include('lenses.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^nested_admin/', include('nested_admin.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]