from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.

def index(request):
    template_name = "my_resume/index.html"
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()    
        return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")
    return render(request, 'my_resume/index.html')