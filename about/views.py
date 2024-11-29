from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):
    """
    Displays posts page
    """
    template_name = 'about/about.html'