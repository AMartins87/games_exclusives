from django.urls import path
from . import views

urlpatterns = [
    path('<game_id>', views.game_reviews, name='game_reviews'),
    path('add_review/<game_id>/', views.add_review, name='add_review'),
]