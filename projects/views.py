from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def projects(request):
    return HttpResponse("Hello, world. You're at the projects page.")


def project(request, pk):
    return HttpResponse(f"You're looking at project {pk}.")
