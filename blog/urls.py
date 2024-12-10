from . import views
from django.urls import path
from .views import AllPosts

urlpatterns = [
    path('', AllPosts.as_view(), name='blog'), 
    path('ingredient/<str:ingredient>/', AllPosts.as_view(), name='blog_by_ingredient'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/like/', views.like_post, name='like_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]