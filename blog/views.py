from django.http import HttpResponse

# Create your views here.
def land_page_view(request):
    return HttpResponse("<h1>This is a test</h1>")