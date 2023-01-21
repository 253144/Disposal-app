from .models import Contener, Price
from rest_framework import serializers


class ContenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contener
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'