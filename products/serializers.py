from rest_framework import serializers
from transactions.serializers import SeasonsSerializers
from rest_framework import status

from .models import *


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class SeedSerializer(serializers.ModelSerializer):
    season = SeasonsSerializers(read_only=True)

    class Meta:
        model = Seed
        fields = '__all__'


class SeedOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        amount = attrs.get("per_cost", None)
        pay_type = attrs.get("payment_type", None)
        print(amount)
        print(pay_type)

        if pay_type == 'CH' and amount is None:
            raise serializers.ValidationError("Amount should not be none", code=status.HTTP_400_BAD_REQUEST)
        elif pay_type == 'CT' and amount is not None:
            raise serializers.ValidationError("Amount should be none", code=status.HTTP_400_BAD_REQUEST)
        return attrs

    class Meta:
        model = Feed
        fields = '__all__'


class OilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oil
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = '__all__'


class MiscellaneousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miscellaneous
        fields = '__all__'
