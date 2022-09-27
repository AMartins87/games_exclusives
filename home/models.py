from django.db import models


class Contact(models.Model):
    """
    To contact the shop owner.
    """
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=''
    )
    email = models.EmailField()
    message = models.TextField(
        max_length=350,
        null=False,
        blank=False
    )
    date_sent = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Meta data for the contact.
        """
        ordering = ('-date_sent',)

    def __str__(self):
        return f'{self.email}'
