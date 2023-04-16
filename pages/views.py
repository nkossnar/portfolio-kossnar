from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ContactForm
from django.core.mail import send_mail, get_connection

def home_page_view(request):
    return HttpResponse("Hello, World!")

def home(request):
    template = loader.get_template('pages/maintemplate.html')
    return HttpResponse(template.render())

def react(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render())

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['nkossnar@gmail.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {'form': form, 'submitted': submitted})
    #return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})