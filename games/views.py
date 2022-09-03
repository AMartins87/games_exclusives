from django.shortcuts import render, get_object_or_404
from .models import Game


def all_games(request):
    """ A view to show all games, including sorting and search queries """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to show individual game details """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game_detail.html', context)
