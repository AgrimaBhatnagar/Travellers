from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('specialoffers',views.specialoffers,name='specialoffers'),
    path('africa',views.africa,name='Africa'),
    path('antartica',views.antartica,name='Antarica'),
    path('asia',views.asia,name='Asia'),
    path('australia',views.australia,name='Australia'),
    path('europe',views.europe,name='Europe'),
    path('northamerica',views.northamerica,name='North America'),
    path('southamerica',views.southamerica,name='South America'),
    path('custum',views.custum,name='Customise Your Trip'),
    
    
]
