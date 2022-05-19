from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, models
from rest_framework import status


# Create your views here.


class MedicineDetails(APIView):

    def get(self, request):
        medicines = models.Medicine.objects.all()
        serializer = serializers.MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
