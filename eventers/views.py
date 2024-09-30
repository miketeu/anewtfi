from django.http import HttpResponse
from django.template import loader
from .models import Eventers

# Create your views here.
def eventers(request):
    myeventers = Eventers.objects.all().values()
    template = loader.get_template('all_eventers.html')
    context = {
        'myeventers': myeventers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myeventers = Eventers.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myeventers': myeventers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())