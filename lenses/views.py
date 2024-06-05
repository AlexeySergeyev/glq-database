from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from django.http import HttpResponse
from .models import *


def main(request):
    """
    Renders the main page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response for the main page.
    """
    return render(request, 'lenses/main.html')

def index(request):
    """
    Renders the index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response for the index page.
    """
    latest_gls_list = GLObject.objects.all()
    #.order_by('gl_alpha')
    #context = {'latest_gls_list': latest_gls_list}
    paginator = Paginator(latest_gls_list, 10) 
    page = request.GET.get('page')
    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        context = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context = paginator.page(paginator.num_pages)
    return render(request, 'lenses/index.html',{'latest_gls_list': context})

def search(request):
    """
    Renders the search page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response for the search page.
    """
    return render(request, 'lenses/search.html')

def links(request):
    """
    Renders the links page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response for the links page.
    """
    return render(request, 'lenses/links.html')

def contacts(request):
    """
    Renders the contacts page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response for the contacts page.
    """
    return render(request, 'lenses/contacts.html')

def detail(request, globject_id):
    """
    Renders the detail page for a specific GLObject.

    Parameters:
    - request: The HTTP request object.
    - globject_id: The ID of the GLObject.

    Returns:
    - A rendered HTML response for the detail page.
    """
    globject = get_object_or_404(GLObject, pk=globject_id)
    return render(request, 'lenses/detail.html', {'globject': globject})

