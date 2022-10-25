""" Basket contexts"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Game


def basket_contents(request):
    """
    Puts together basket contents
    """
    basket_items = []
    total = 0
    game_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        game = get_object_or_404(Game, pk=item_id)
        total += quantity * game.price
        game_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'game': game,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'game_count': game_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
