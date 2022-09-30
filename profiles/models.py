from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from games.models import Game


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Favourites(models.Model):
    """
    Saves games in shopper's favourites
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    games = models.ManyToManyField(
        Game, through='FavouritesItem',
        related_name='game_favourites'
    )

    def __str__(self):
        return f'Favourites ({self.user})'

class UserFavourites (models.Model):
    '''Model to store user wishlist items'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gamess = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return self.user.username


class FavouritesItem(models.Model):
    """
    Allows shopper to add games to their favourites
    """
    game = models.ForeignKey(
        Game,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    favourites = models.ForeignKey(
        Favourites,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.game.name
