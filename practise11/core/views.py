from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class home(TemplateView):
    template_name = "core/index.html"
