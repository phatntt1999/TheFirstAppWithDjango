from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.\nMy name is Phat")

def index(request):
    return render(request, "pages/Home.html")

def contact(request):
    return render(request, "pages/Contact.html")

def blog(request):
    return render(request, "pages/Blog.html")
