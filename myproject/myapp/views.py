from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Feature

# Create your views here.
def index(request):
    hour = datetime.now().hour
    greeting = "Good morning" if 5<=hour<12 else "Good afternoon" if hour<18 else "Good evening"
    
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Feature 1'
    feature1.details = 'This is the details of Feature 1'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Feature 2'
    feature2.details = 'This is the details of Feature 2'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Feature 3'
    feature3.details = 'This is the details of Feature 3'
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Feature 4'
    feature4.details = 'This is the details of Feature 4'
    
    features = [feature1, feature2, feature3, feature4]
    
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