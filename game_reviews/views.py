from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from games.models import Game
from .models import GameReview
from .forms import GameReviewForm


@login_required
def add_review(request, game_id):
    """ Add game review """
    game = get_object_or_404(Game, pk=game_id)
    form = GameReviewForm

    if request.method == 'POST':
        previous_review = GameReview.objects.filter(
            reviewer=request.user, game=game,
        ).exists()
        if previous_review:
            # If shopper left a review for this game
            # error message will be displayed
            messages.error(request,
                           'You have already left a review '
                           f'for {game.name} !')
        else:
            # If no previous review exists
            form = GameReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = User.objects.get(
                    username=request.user.username)
                review.game = game
                review.save()
                messages.success(request, 'You successfully added review!')
                return redirect(reverse(
                    'game_detail', kwargs={"game_id": game.id}))
            else:
                messages.error(request,
                               'Failed to add review.'
                               'Please ensure the form is valid')
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
            messages.info(request, 'You successfully updated'
                          ' your game review!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed update review.'
                           'Please ensure the form is valid.')
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

    messages.info(request, 'You successfully deleted your game review!')
    return redirect(reverse('game_detail', args=[game.id]))
