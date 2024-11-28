# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def land_page_view(request):
#     return HttpResponse("<h1>This is a test</h1>")

class HomePage(TemplateView):
    """
    Displays home page structure"
    """
    template_name = 'base.html'