from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def payment(request):
    return render(request, 'payment.html')
