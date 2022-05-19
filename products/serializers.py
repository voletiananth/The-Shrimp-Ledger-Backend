from rest_framework import serializers

from . import models


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicine
        fields = '__all__'

