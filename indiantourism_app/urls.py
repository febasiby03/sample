from django.urls import path
from . import views

urlpatterns = [
     path('',views.base,name='base'),
     path('extension',views.extension,name='extension'),
     path('home.html',views.home,name='home'),
     path('about.html',views.about,name='about'),
     path('contact.html',views.contact,name='contact'),
     path('gallery.html',views.gallery,name='gallery'),
     path('login.html',views.login,name='login')
 
       

     


]