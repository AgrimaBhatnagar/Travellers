from hello.models import Ccustum
from django.shortcuts import render
from django.http import HttpResponse, response
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'index.html')
    #return HttpResponse("Hello World")
def about(request):
    return render(request,'about.html')
  
def contact(request):
    return render(request,'contact.html')
def specialoffers(request):
    
    return render(request,'specialoffers.html') 
def destinations(request):
    return render (request,'destinations.html')          
def africa(request):
    return render(request,'africa.html')    
def antartica(request):
    return render(request,'antartica.html')
def asia(request):
    return render(request,'asia.html')
def australia(request):
    return render(request,'australia.html')
def europe(request):
    return render(request,'europe.html')       
def northamerica(request):
    return render(request,'northamerica.html')    
def southamerica(request):
    return render(request,'southamerica.html')  
def custum(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        flighttakeofflocation=request.POST.get('flighttakeofflocation')
        flightlandonlocation=request.POST.get('flightlandonlocation')
        duration=request.POST.get('duration')
        hotels=request.POST.get('hotels')

        cus=Ccustum(name=name,phone=phone,email=email,password=password,flighttakeofflocation=flighttakeofflocation,flightlandonlocation=flightlandonlocation,duration=duration,hotels=hotels)
        cus.save()
    return render(request,'custum.html')                  