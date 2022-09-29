from django.contrib import admin

from .models import GameReview


class GameReviewAdmin(admin.ModelAdmin):
    """ List display for games in admin page """
    list_display = (
        'game',
        'rating',
        'reviewer',
        'date',
    )


admin.site.register(GameReview, GameReviewAdmin)
