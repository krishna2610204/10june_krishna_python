from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')

def bestseller(request):
    return render(request,'bestseller.html')

def cart(request):
    return render(request,'cart.html')

def cheackout(request):
    return render(request,'cheackout.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,'shop.html')

def single(request):
    return render(request,'single.html')







