from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from checkout.models import Order
from games.models import Game

from .models import UserProfile, Favourites
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Displays the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed.'
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def favourites(request):
    """
    Renders favourites
    """
    favourites_items = []
    favourites = request.session.get('favourites', {})

    try:
        favourites = Favourites.objects.get(user=request.user)
    except ObjectDoesNotExist:
        favourites = Favourites.objects.create(user=request.user)
    else:
        favourites_items = favourites.games.all()

    if not favourites_items:
        messages.info(request, 'Your favourites list is empty!')

    context = {
        'favourites': favourites,
        'favourites_items': favourites_items,
    }
    return render(request, 'profiles/favourites.html', context)


@login_required
def add_to_favourites(request, game_id):
    """
    Adds game to favourites
    """
    game = get_object_or_404(Game, pk=game_id)

    # Creates favourites list for the user if they don't have one
    favourites, _ = Favourites.objects.get_or_create(user=request.user)

    # Adds game to shopper's favourite's list
    if game in favourites.games.all():
        messages.error(
            request,
            game.name + ' is already in your favourites.'
        )
    else:
        favourites.games.add(game)
        messages.info(
            request,
            'You added ' + game.name + ' to your favourites.'
        )

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favourites(request, game_id):
    """
    Removes a game from the favourites
    """
    favourites = Favourites.objects.get(user=request.user)
    game = get_object_or_404(Game, pk=game_id)

    # Removes game from shopper's favourites
    favourites.games.remove(game)
    messages.info(
        request,
        game.name + ' was removed from your favourites.'
    )

    return redirect(request.META.get('HTTP_REFERER'))
