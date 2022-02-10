import random

import stripe

from rest_framework import viewsets
from rest_framework.response import Response

from config import STRIPE_SECRET_KEY
from middleware_api.models import StripeResponse, StripeRequest
from middleware_api.utils import parse_date, mask
from middleware_api.serializers import RequestSerializer, ResponseSerializer

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
            # Split date in month and year
            data = parse_date(data)
            request_serializer = RequestSerializer(data=data)
            request_validness = request_serializer.is_valid(raise_exception=True)
            # Log the request
            charge_request = StripeRequest.objects.create(
                trans_id=request_serializer.validated_data['trans_id'],
                cc_num=mask(request_serializer.validated_data['cc_num']),  # We mask the card number
                cvv=mask(request_serializer.validated_data['cvv']),  # and the cvc
                exp_month=request_serializer.validated_data['exp_month'],
                exp_year=request_serializer.validated_data['exp_year'],
                errors=request_serializer.errors if request_serializer.errors else "",
            )
            if request_validness:
                # Request the token with the card credentials
                token = stripe.Token.create(
                    card={
                        "number": request_serializer.validated_data['cc_num'],
                        "exp_month": request_serializer.validated_data['exp_month'],
                        "exp_year": request_serializer.validated_data['exp_year'],
                        "cvc": request_serializer.validated_data['cvv'],
                    },
                )
                # Send the charge request with extra payload
                response = stripe.Charge.create(
                    amount=random.randint(1, 1000),
                    currency="usd",
                    source=token.id,
                )
                # Log the response in db
                charge_response = StripeResponse.objects.create(
                    stripe_id=response.id,
                    status=response.status,
                    amount=response.amount,
                    action=response.object,
                    request_id=charge_request,
                )
                response_serializer = ResponseSerializer(charge_response)
                return Response(response_serializer.data)
            else:
                return Response(request_serializer.errors, status=400)
        except Exception as e:
            return Response(status=500)
