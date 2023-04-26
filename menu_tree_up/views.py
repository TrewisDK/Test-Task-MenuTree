from django.shortcuts import render
from django.views import View
from .models import MenuPoint


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Test(View):
    def get(self, request):
        return render(request, 'index.html')

