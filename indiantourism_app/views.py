from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def extension(request):
    return render(request,'extension.html')

def base(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def login(request):
    return render(request,'login.html')


