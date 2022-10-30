from django.shortcuts import render
from django.http import HttpResponse


def notes(request):
    return HttpResponse ("Hello, world. You're at the polls index.")

def notes1(request):
    return render (request, 'notes/detail.html', {'question': 'What is the password','list1': [1,2,3,4,5],})
