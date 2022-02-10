import random

import stripe

from rest_framework import viewsets
from rest_framework.response import Response

from config import STRIPE_SECRET_KEY
from middleware_api.models import Request
from middleware_api.processor import parse_date, mask
from middleware_api.serializers import RequestSerializer

stripe.api_key = STRIPE_SECRET_KEY


class ChargeViewSet(viewsets.ViewSet):
    """
    A viewset for sending and logging charges
    """
    serializer_class = RequestSerializer
    api_url = 'https://api.stripe.com/v1/'

    def create(self, request):
        data = request.data.copy()
        try:
            data = parse_date(data)
            serializer = RequestSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                charge_request = Request.objects.create(
                    cc_num=mask(serializer.validated_data['cc_num']),
                    exp_month=serializer.validated_data['exp_month'],
                    exp_year=serializer.validated_data['exp_year'],
                    trans_id=serializer.validated_data['trans_id'],
                    cvv=mask(serializer.validated_data['cvv']),
                )
                token = stripe.Token.create(
                    card={
                        "number": serializer.validated_data['cc_num'],
                        "exp_month": serializer.validated_data['exp_month'],
                        "exp_year": serializer.validated_data['exp_year'],
                        "cvc": serializer.validated_data['cvv'],
                    },
                )
                charge_response = stripe.Charge.create(
                    amount=random.randint(0, 1000),
                    currency="usd",
                    source=token.id,
                )
                return Response(charge_response)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response(e.error)
