from django.urls import path
from .views import land_page_view

urlpatterns = [
    path("", land_page_view)
]