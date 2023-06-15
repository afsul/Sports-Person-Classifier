from django.shortcuts import render, redirect

# Create your views here.

def image_classify(request):
    print("hello world this is the world")
    return render(request, 'app.html')
