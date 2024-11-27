from django.urls import path
from .views import land_page_view
from cloudinary.models import CloudinaryField

urlpatterns = [
    path("", land_page_view)
]