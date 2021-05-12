from django.shortcuts import render
from django.conf import settings


# Create your views here.
def hello(request):
  return render(request, "hello.html")
