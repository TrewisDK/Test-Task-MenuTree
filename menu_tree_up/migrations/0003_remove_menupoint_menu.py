# Generated by Django 4.2 on 2023-04-25 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_tree_up', '0002_menu_menupoint_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menupoint',
            name='menu',
        ),
    ]
