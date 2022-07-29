from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contacts

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for contacting")
    else:
        form = ContactForm()
    
    return render(request,"contact.html", {"contact_form":form})

#from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render, redirect
#from .forms import ContactForm

#def contactView(request):
 #   if request.method == 'GET':
  #      form = ContactForm()
  #  else:
   #     form = ContactForm(request.POST)
   #     if form.is_valid():
    #        subject = form.cleaned_data['name']
   #        from_email = form.cleaned_data['from_email']
   #        message = form.cleaned_data['message']
    #        try:
    #           send_mail(subject, message, from_email, ['admin@example.com'])
    #       except BadHeaderError:
    #           return HttpResponse('Invalid header found.')
    #        return redirect('success')
   #return render(request, "email.html", {'form': form})

#def successView(request):
#    return HttpResponse('Success! Thank you for your message.')
    