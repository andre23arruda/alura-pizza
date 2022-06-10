from rest_framework import serializers
from ..models import Dish


class DishSerializer(serializers.ModelSerializer):
    '''Dish Serializer'''

    class Meta:
        model = Dish
        fields = '__all__'