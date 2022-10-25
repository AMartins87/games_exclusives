from django.contrib import admin
from .models import Game, Category


class GameAdmin(admin.ModelAdmin):
    """
    Tells admin which fields to display
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    """
    Sorts the products by SKU using the ordering attribute
    """
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
     Creates admin display in database
     """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
