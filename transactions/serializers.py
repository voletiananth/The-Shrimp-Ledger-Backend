from rest_framework import serializers

from products.models import *


class SeasonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'



