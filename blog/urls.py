from .import views
from django.urls import path
from cloudinary.models import CloudinaryField

urlpatterns = [
    path(views.HomePage.as_view(), name='home'),
]