from rest_framework import serializers

from item.models import Item


class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'