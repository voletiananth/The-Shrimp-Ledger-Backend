from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, models
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class MedicineDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MedicineSerializer

    def get(self, request):
        medicines = models.Medicine.objects.filter(user=self.request.user)
        serializer = serializers.MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeedDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SeedSerializer

    def get(self, request):
        seeds = models.Seed.objects.filter(user=self.request.user)
        data = serializers.SeedSerializer(seeds, many=True).data
        return Response(data)

    def post(self, request):
        user = self.request.user
        season = models.Season.objects.create(user=user)
        serializer = serializers.SeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, season=season)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FeedSerializer

    def get(self, request):
        feeds = models.Feed.objects.filter(user=self.request.user)
        data = serializers.FeedSerializer(feeds, many=True).data
        return Response(data)

    def post(self, request):
        serializer = serializers.FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OilDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OilSerializers

    def get(self, request):
        oil = models.Oil.objects.filter(user=self.request.user)
        serializer = serializers.OilSerializers(oil, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.OilSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepairDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RepairSerializer

    def get(self, request):
        repair = models.Repair.objects.filter(user=self.request.user)
        serializer = serializers.RepairSerializer(repair, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.RepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MiscellaneousDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MiscellaneousSerializer

    def get(self, request):
        miscellaneous = models.Miscellaneous.objects.filter(user=self.request.user)
        serializer = serializers.MiscellaneousSerializer(miscellaneous, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MiscellaneousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
