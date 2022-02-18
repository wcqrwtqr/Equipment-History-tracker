from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jobindex(requst):
    return HttpResponse("He there this is for the JObs")
