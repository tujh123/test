from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse('This is home page')
    context = {

    }
    return render(request, 'home.html', context)
