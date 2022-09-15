from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LWQzwE0HgyyghLfs6gxGEyStLYtHxdXABvl'
                             '86cbVd3LcCP1zONrXf9JMlfMyIbSxSpllWbbw5hXho0Y'
                             'pwdGIGHW00LX4fxodh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
