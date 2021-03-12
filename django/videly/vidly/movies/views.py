from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
#    take all objects of movie
   Movie.objects.all()
   output =  ', '.join([m.title for m in movies])
#   list comprehension to use title of movie
   return HttpResponse(output)