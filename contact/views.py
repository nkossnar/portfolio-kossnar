from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_req(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})