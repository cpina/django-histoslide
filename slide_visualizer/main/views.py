from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')
