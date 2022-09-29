from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from games.models import Game


class GameReview(models.Model):
    """ Model for game review and rating """

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
                                 MinValueValidator(1),
                                 MaxValueValidator(5)],
                                 default=1, null=False, blank=False)
    title = models.CharField(max_length=150, default="Game Review")
    review = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
