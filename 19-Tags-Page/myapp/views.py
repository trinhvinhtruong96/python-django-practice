from django.shortcuts import render
from myapp.models import Flower

def index(request): # < here
  flowers = Flower.objects.all()
  return render(request, 'myapp/index.html', {'flowers': flowers })

def tags(request, slug=None): # < here
  flowers = Flower.objects.filter(tags__slug=slug)
  return render(request, 'myapp/index.html', {'flowers': flowers })