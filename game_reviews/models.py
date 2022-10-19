from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class GameReview(models.Model):
    """ Model for game reviews """
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default="Game Review")
    review = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.review)
