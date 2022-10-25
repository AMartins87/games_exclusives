""" Config file for Checkout app"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Config for Checkout app
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
