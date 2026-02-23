from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'name': 'Ahmed',
        'age': 25,
        'skills': ['Python', 'Django', 'HTML'],
        'is_student':False,
    }
    
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse("about!")