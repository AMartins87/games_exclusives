from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from games.models import Game
from .models import GameReview
from .forms import GameReviewForm


@login_required
def add_review(request, game_id):
    """ Add game review """

    game = Game.objects.get(pk=game_id)

    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.game = game
            review.save()
            messages.success(request, 'You successfully added'
                             'your game review !')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed to add review. \
                                     Please ensure the form is valid.')
    else:
        form = GameReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'game': game
    }

    return render(request, template, context)


@login_required
def edit_review(request, game_id, review_id):
    """ Edit game review """

    game = Game.objects.get(pk=game_id)
    review = GameReview.objects.get(pk=review_id)

    if request.method == 'POST':
        form = GameReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.game = game
            review.save()
            messages.success(request, 'You successfully updated'
                             'your game review!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed update review. \
                           Please ensure the form is valid.')
    else:
        form = GameReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'game': game,
        'review': review
    }

    return render(request, template, context)


@login_required
def delete_review(request, game_id, review_id):
    """ Delete game review """

    game = get_object_or_404(Game, pk=game_id)
    review = get_object_or_404(GameReview, pk=review_id)
    review.delete()

    messages.success(request, 'You successfully deleted your game review!')
    return redirect(reverse('game_detail', args=[game.id]))
