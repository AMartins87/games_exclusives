from django import forms
from .models import GameReview


class GameReviewForm(forms.ModelForm):
    """ Form to add game review """
    class Meta:
        model = GameReview
        fields = ('title',
                  'review')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
