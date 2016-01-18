from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class MainPage(TemplateView):
    template_name = "agency.html"


class TestPage(TemplateView):
    template_name = "portfolio.html"
