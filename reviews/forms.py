from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Add / Edit Review
    """
    class Meta:
        model = Review
        exclude = ('rating', 'review')


    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, sets autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'reviews': 'Write your review here',
        }

        self.fields['review'].widget.attrs['autofocus'] = True


