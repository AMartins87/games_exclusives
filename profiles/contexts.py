from .models import Favourites


def favourites_context(request):
    """
    Passes current favourites or none to context
    """
    favourites_items = []
    if request.user.is_authenticated:
        try:
            favourites = Favourites.objects.get(user=request.user)
            favourites_items = favourites.games.all()
        except Favourites.DoesNotExist:
            favourites_items = []

    context = {
        'favourites_items': favourites_items,
    }

    return context
