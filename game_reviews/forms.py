from django import forms

from .models import GameReview


# Options for game review 'rating' dropdown
RATING_CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))


class GameReviewForm(forms.ModelForm):
    """ Form to add game review """
    class Meta:
        model = GameReview
        fields = ('rating',
                  'title',
                  'review')

        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES)
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
