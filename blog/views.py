from django.shortcuts import render, get_object_or_404, reverse
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

def post_detail(request, slug):
    """
    Display an individual post :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.order_by("created_on")
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )