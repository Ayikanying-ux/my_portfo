from django.shortcuts import render
from .forms import *
from django.http.response import HttpResponseRedirect


# Create your views here.

def index(request):
    if request.method == "POST":
        form_class = ContactForm(request.POST)
        if form_class.is_valid():
            Firstname = form_class.cleaned_data['Firstname']
            Lastname = form_class.cleaned_data['Lastname']
            email = form_class.cleaned_data['email']
            message = form_class.cleaned_data['message']
            
            return HttpResponseRedirect('thankyou')
    else:
        form_class = ContactForm(initial={'user':request.user,'otherstuff':'otherstuff'})

    return render(request, "base/index.html", {
        'form': form_class
    })

def thankyou(request):
    return render(request, "base/thankyou.html")
