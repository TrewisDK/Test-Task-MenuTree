from django import template
from menu_tree_up.models import Menu

register = template.Library()


@register.inclusion_tag("custom_tags/menu_tags/menu_template.html")
def draw_menu(menu_name):
    menu_points = Menu.objects.get(name=menu_name).current_menu_points.all
    return {"menu_points" : menu_points}

