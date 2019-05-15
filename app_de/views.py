from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def indexx(request):
    return HttpResponse("go")

def detail(request,question_id):
    return HttpResponse("you looking question %s" % question_id)

def results(request,question_id):
    response = "You're looking at the %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're votiong %s." % question_id)

