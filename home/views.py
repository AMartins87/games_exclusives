from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
from django.conf import settings


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ Renders the contact page """
    contact_form = ContactForm(data=request.POST)
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():

            full_name = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            html = render_to_string(
                'home/message_sent.html', {
                    'full_name': full_name,
                    'email': email,
                    'message': message
                }
            )

            contact_form = contact_form.save(commit=False)
            contact_form.save()
            send_mail(
                'Contact us',
                'Thank you for contacting us!',
                'aneta.martinss@gmail.com',
                {email},
                fail_silently=False,
            )
            messages.info(request, 'Message sent successfully!')
            return redirect('home')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'home/contact.html', context)
