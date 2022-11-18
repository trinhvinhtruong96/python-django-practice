from django.shortcuts import render, get_object_or_404
from myapp.models import Flower

def index(request): # < here
  flowers = Flower.objects.all()
  return render(request, 'myapp/index.html', {'flowers': flowers })

def detail(request, slug=None): # < here
  flower = get_object_or_404(Flower, slug=slug)
  return render(request, 'myapp/detail.html', {'flower': flower})

