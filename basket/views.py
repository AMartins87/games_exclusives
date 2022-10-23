""" Basket app views """
from django.shortcuts import (
     render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from games.models import Game


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Adds quantity of chosen game to the shopping basket """

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f' You added {game.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjusts the quantity of chosen game to selected amount """

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {game.name} quantity to {basket[item_id]}'
            )
    else:
        basket.pop(item_id)
        messages.success(request, f'You have succcessfully removed {game.name}'
                         ' from your basket!')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""
    try:
        game = get_object_or_404(Game, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'You have succcessfully removed {game.name}'
                         ' from your basket!')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing game: {e}')
        return HttpResponse(status=500)
