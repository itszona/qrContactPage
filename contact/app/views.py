from django.shortcuts import render
from .models import Contacts
from django.http import HttpResponse
# Create your views here.
def contact(request):
    if request.method == "POST":
        detail=Contacts()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        detail.name=name
        detail.email=email
        detail.subject=subject
        detail.save()
        return HttpResponse("Thanks for contacting")
    return render(request,"contact.html")