from django.views.generic import TemplateView

# Create your views here.

class AllPosts(TemplateView):
    """
    Displays posts page
    """
    template_name = 'blog/blog.html'