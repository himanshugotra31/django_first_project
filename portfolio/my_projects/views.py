from django.shortcuts import render
from django.http import HttpResponse

projects=[
    {
        "id":1,
        "name":"Balls Screensaver",
        "Languages":['C++'],
        "Additional Libraries":[],
        "Description":"Displays random balls and terrain in 3D which can collide",
        "url":"we will insert some random url here"
    },
    {
        "id":2,
        "name":"AC Circuit Solver",
        "Languages":['C++'],
        "Additional Libraries":["Matrix Computation Library","SVG Rendering"],
        "Description":"""Given circuit as a text file input, render it on HTML page, 
                         also will show the current's and voltage's value""",
        "url":"we will insert some random url here"
    }
]

def index(request):
    return HttpResponse('Hello Derick!!!')

def home(request):
    # render the home.html template for the request with the projects variable
    return render(request,'my_projects/home.html', context= {"my_projects" : projects})

def project(request,id):
    # here it will find the project details for this id
    return 

# Create your views here.
