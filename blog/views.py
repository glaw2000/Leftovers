from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.fk_user_id = request.user
            comment.fk_post_id = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )