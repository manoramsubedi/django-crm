from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    #return HttpResponse("HELLO ALL!")
    return render(request, 'webapp/index.html')

def about(requst):
    return HttpResponse("THIS IS ABOUT SECTION")


