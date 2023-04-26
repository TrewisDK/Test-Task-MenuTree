from django import template
from menu_tree_up.models import Menu

register = template.Library()


@register.inclusion_tag("custom_tags/menu_tags/menu_template.html", takes_context=True)
def draw_menu(context, menu_name):
    """ Функция отвечающая за отображение меню на странице
    Принимает аргументы context - для получения из request текущего url адреса, а так же menu-name для получения меню,
    которое нужно отобразить """

    # По 1 запросу получаем меню, а затем получаем из него его пункты
    menu_points = Menu.objects.get(name=menu_name).current_menu_points.all
    return {"menu_points": menu_points, 'request': context['request']}
