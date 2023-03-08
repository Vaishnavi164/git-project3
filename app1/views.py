from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sonu(request):
    return HttpResponse('<h1>sonu is good positive thinker</h1>')

def chinchan(request):
    return HttpResponse('<h1>chinchan is the best cartoon</h1>')    
