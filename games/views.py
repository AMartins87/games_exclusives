from django.shortcuts import render
from .models import Game


def all_games(request):
    """ A view to show all products, including sorting and search queries """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)
