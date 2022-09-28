from django.contrib import admin
from .models import UserProfile, Favourites, FavouritesItem


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'default_phone_number')
    list_filter = ('user',)
    search_fields = ('user', 'default_phone_number')

admin.site.register(Favourites)

admin.site.register(FavouritesItem)
