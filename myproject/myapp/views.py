from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'greeting' : 'Good morning',
        'name' : 'Ethan'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('<h1>Hello world!</h1>') 