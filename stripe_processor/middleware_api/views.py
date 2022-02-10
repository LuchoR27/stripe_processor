import stripe
from django.shortcuts import render

from rest_framework import viewsets

from config import STRIPE_SECRET_KEY
from middleware_api.serializers import RequestSerializer

stripe.api_key = STRIPE_SECRET_KEY


class ChargeViewSet(viewsets.ViewSet):
    """
    A viewset for sending and logging charges
    """
    serializer_class = RequestSerializer

    def create(self, request):
        data = request.data.copy()
        print(request)
