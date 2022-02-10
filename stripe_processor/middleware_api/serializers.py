from rest_framework import serializers

from middleware_api.models import StripeRequest, StripeResponse


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripeRequest
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripeResponse
        fields = '__all__'
