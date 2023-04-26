from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField("Название меню", max_length=30)

    def __str__(self):
        return self.name


class MenuPoint(models.Model):
    name = models.CharField("Назавание пункта", max_length=30)
    menu = models.ForeignKey(Menu, related_name='current_menu_points', on_delete=models.CASCADE, null=True)
    url = models.CharField("URL", max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def check_absolute_url(self):
        if self.url:
            return self.url
        else:
            reverse(self.url)
