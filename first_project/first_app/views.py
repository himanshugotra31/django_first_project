from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def age_page(request,age):
    return HttpResponse(

        '''
        <h1>
        '''
        +age+
        '''
        </h1>
        '''
    )
def intro(request,name,age):
    return HttpResponse("Hi "+name+". You are "+str(age))

def about_me(request):
    return HttpResponse(
    '''
    <h1>Hey I am derick</h1>
    <h2>I play soccer</h2>
    <p>
    Soccer
    Ronaldo
    Messi
    </p>
    '''
    )
