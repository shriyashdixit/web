from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
 
def index(request):
    data = {"content": "Gfg is the best"}
    return render(request, "home_page.html", data)