from .models import GameReview


def game_reviews(request):
    """ Function to return game reviews to the context """
    game_reviews = GameReview.objects.all()

    context = {
        'game_reviews': game_reviews
    }

    return context
