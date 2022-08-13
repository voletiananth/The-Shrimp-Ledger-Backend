import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers,serializers2
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.


class SeasonApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SeasonsSerializers

    def get(self, request):
        seasons = models.Season.objects.filter(user=self.request.user)
        serializer = serializers.SeasonsSerializers(seasons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SeasonsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        date = request.GET.get("date", datetime.date.today().strftime('%Y-%m-%d'))
        print(date)
        response_data = serializers2.TransactionSerializers(data={
            "date": date,
        },
            user=self.request.user
        )
        if response_data.is_valid():
            return Response(response_data.data)
        return Response(response_data.errors, status=status.HTTP_400_BAD_REQUEST)
