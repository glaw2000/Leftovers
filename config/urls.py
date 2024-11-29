"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls'), name='home'),
    path('blog/', include('blog.urls'), name='blog'),
    path('about/', include('about.urls'), name='about')
]
