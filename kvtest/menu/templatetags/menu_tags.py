from django import template
from menu.models import Menu
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('menu-tag.html')
def draw_menu(name, request):
    menu = Menu.objects.filter(name=name).first()
    links = menu.links.filter(parent__isnull=True)

    return {'menu': menu, 'links': links, 'request': request}
