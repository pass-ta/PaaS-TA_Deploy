from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    Function that shows the hello world with an Http Response.
    """
    return HttpResponse("Hello This is a Django App TEST 😄")
