from rest_framework import serializers

from products.models import *
from products.serializers import *
from products.views import MedicineDetails


class TransactionSerializers(serializers.Serializer):
    date = serializers.DateField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(**kwargs)

    def to_representation(self, instance):
        self.date = instance['date']
        instance['medicine'] = self._medicine()
        instance['feed'] = self._feed()
        instance['oil'] = self._oil()
        instance['repair'] = self._repair()
        instance['miscellaneous'] = self._miscellaneous()
        return instance

    def _medicine(self):
        medicine = Medicine.objects.filter(user=self.user, date_created=self.date)
        medicine_serializer = MedicineSerializer(medicine, many=True)
        return medicine_serializer.data

    def _feed(self):
        feed = Feed.objects.filter(user=self.user, date_created=self.date)
        feed_serializer = FeedSerializer(feed, many=True)
        return feed_serializer.data

    def _oil(self):
        oil = Oil.objects.filter(user=self.user, date_created=self.date)
        oil_serializer = OilSerializers(oil, many=True)
        return oil_serializer.data

    def _repair(self):
        repair = Repair.objects.filter(user=self.user, date_created=self.date)
        repair_serializer = RepairSerializer(repair, many=True)
        return repair_serializer.data

    def _miscellaneous(self):
        miscellaneous = Miscellaneous.objects.filter(user=self.user, date_created=self.date)
        miscellaneous_serializer = MiscellaneousSerializer(miscellaneous, many=True)
        return miscellaneous_serializer.data
