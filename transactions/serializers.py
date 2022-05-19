from rest_framework import serializers
from . import models


class SeasonsSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Season
        fields = '__all__'
