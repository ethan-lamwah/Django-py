from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    hour = datetime.now().hour
    greeting = "Good morning" if 5<=hour<12 else "Good afternoon" if hour<18 else "Good evening"
    
    context = {
        'greeting' : greeting,
        'name' : 'Ethan'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('<h1>Hello world!</h1>') 
    
def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})