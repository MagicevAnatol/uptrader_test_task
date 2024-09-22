from django.shortcuts import render, get_object_or_404

from .models import MenuItem


def index(request):
    return render(request, 'menu/index.html')


def dynamic_page(request, named_url):
    menu_item = get_object_or_404(MenuItem, named_url=named_url)
    return render(request, 'menu/dynamic_page.html', {'menu_item': menu_item})