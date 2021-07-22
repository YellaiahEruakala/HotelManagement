from django.shortcuts import render, redirect
from .models import Coffee
# Create your views here.
def index(request):
    coffee = Coffee.objects.all()
    return render(request, 'index.html', {'coffee':coffee})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#def email(request):
#    return redirect('https://mail.google.com/mail')