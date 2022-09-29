from django.db import models
from django.contrib.auth.models import User


from games.models import Game
from profiles.models import UserProfile
from checkout.models import OrderLineItem


class Review(models.Model):

    RATINGS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    rating = models.IntegerField(choices=RATINGS)
    review_body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    order_line = models.ForeignKey(OrderLineItem, blank=False, null=False, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title
