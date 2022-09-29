from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from games.models import Game 
from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


def game_reviews(request, game_id):
    """ Shows individual game review """

    reviews = get_object_or_404(Reviews, pk=game_id)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/game_reviews.html', context)


@login_required
def add_review(request, game_id):
    """ Add game review view"""

    game = get_object_or_404(Game, pk=game_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form_data = {
            'ratings': request.POST['ratings'],
            'comments': request.POST['comments'],
        }

    context = {
        'game': game,
    }

    return render(request, 'reviews/add_review.html', context)