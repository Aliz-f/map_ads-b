from rest_framework.exceptions import APIException
from rest_framework import serializers, status

from django.utils.encoding import force_str

from .models import dataFlight

class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None: self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_str(detail)}
        else:
            self.detail = {'detail': force_str(self.default_detail)}

class dataFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=dataFlight
        fields = '__all__'
    
    def create(self, validated_data):
        return dataFlight.objects.create(**validated_data)