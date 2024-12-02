from django.views.generic import ListView
from .models import Post

# Create your views here.

class AllPosts(ListView):
    """
    Displays listing of all posts
    """
    model = Post
    queryset = Post.objects.order_by("created_on")
    template_name = 'blog/blog.html'
    context_object_name = 'items'
    paginate_by = 9
