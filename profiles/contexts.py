from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Game
from .models import Favourites


def favourites_context(request):
    """
    Displays favourites
    """
    favourites_items = []
    favourites_count = 0
    favourites = request.session.get('favourites', {})

    if request.user.is_authenticated:
        return {
            'favourites_count': Favourites.objects.filter(user=request.user).count()
        }
    else:
        return {
            'favourites_count': favourites_count,
        }

    context = {
        'favourites_items': favourites_items,
        'favourites_count': favourites_count,
    }

    return context
