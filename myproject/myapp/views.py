from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Feature

# Create your views here.
def index(request):
    hour = datetime.now().hour
    greeting = "Good morning" if 5<=hour<12 else "Good afternoon" if hour<18 else "Good evening"
    
    features = Feature.objects.all()
    
    context = {
        'greeting' : greeting,
        'name' : 'Ethan',
        'features' : features
    }
    return render(request, 'index.html', context)
    # return HttpResponse('<h1>Hello world!</h1>') 
    
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})