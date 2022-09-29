from django import template
from game_reviews.models import GameReview


register = template.Library()


@register.filter(name='review_count')
def review_count(game_id):
    reviews = GameReview.objects.all()
    game_reviews = 0

    for review in reviews:
        if game_id == review.game.id:
            game_reviews += 1

    return
