"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('about/', include('about.urls'), name='about'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name='blog'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('landing.urls'), name='home')
]
