from django.contrib import admin
from django.urls import path
from menu_tree_up.views import *

# Здесь прописаны тестовы url и url админпанели
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('test/', Test.as_view(), name="test"),
    path('plamakarotatod/', Test.as_view(), name="plus")

]
