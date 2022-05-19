from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class SeasonApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        seasons = models.Season.objects.all()
        serializer = serializers.SeasonsSerializers(seasons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SeasonsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.instance.user = request.user
