from rest_framework import serializers

from middleware_api.models import Request


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'
