from . import views
from django.urls import path
from .views import AllPosts

urlpatterns = [
    path('', AllPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]