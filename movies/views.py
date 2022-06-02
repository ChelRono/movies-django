import json
from django.shortcuts import render
from django.http  import HttpResponse
from urllib import request
from .requests import get_movie,get_movies

# Create your views here.
def index(request):
    
   
    
    return render(request,'index.html')

def api(req):
    res=request.urlopen('https://api.themoviedb.org/3/movie/popular?api_key=03365ca436907df40a7728f1a0ace963')
    print(res)
    results=res.read()
    print(type(results))
    data=json.loads(results)
    print(type(data))
    popular_movies = get_movies('popular')
    print(popular_movies)
    upcoming_movie = get_movies('upcoming')
    print(upcoming_movie)
    now_showing_movie = get_movies('now_playing')
    print(now_showing_movie)
    
    return render(req,'api.html',{'data':data['results'],'popular':popular_movies,'upcoming':upcoming_movie,'now_playing':now_showing_movie})