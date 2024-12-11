from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):
    """
    Displays About page
    """
    template_name = 'about/about.html'