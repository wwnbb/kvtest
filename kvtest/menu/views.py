from django.shortcuts import render
from .models import Menu

def index(request):
    menu = Menu.objects.first()
    links = menu.links.filter(parent__isnull=True)
    return render(request, 'menu.html', {'links': links})
