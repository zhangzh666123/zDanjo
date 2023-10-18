from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def show(request, id):
    return HttpResponse("app2 show function, int key is" + str(id))
