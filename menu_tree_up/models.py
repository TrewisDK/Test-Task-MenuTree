from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """ Модель меню, нужно для того что-бы вызывать меню по name в соответсвии с ТЗ """
    name = models.CharField("Название меню", max_length=30)

    def __str__(self):
        return self.name


class MenuPoint(models.Model):
    """ Модель пунктов меню """
    # Название пункта меню
    name = models.CharField("Назавание пункта", max_length=30)
    # Отношение к модели меню для плучения пунктов при вызове меню
    menu = models.ForeignKey(Menu, related_name='current_menu_points', on_delete=models.CASCADE, null=True)
    # URL адресс меню
    url = models.CharField("URL", max_length=100)
    # Родительский элемент пункта меню, ссылается сам на имеет related_name для получения дочерних элеменов пункта меню
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url.startswith("http"):
            return self.url
        else:
            return reverse(f"{self.url}")
