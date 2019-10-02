from django.shortcuts import render
from rest_framework import viewsets
from .models import Prod1
from .serializers import ProductsSerializer
from rest_framework.views import APIView, Response


class ProductsViewSet(viewsets.ModelViewSet, APIView):
    queryset = Prod1.objects.all()
    serializer_class = ProductsSerializer


class CustomView(APIView):
    def get(self):
        return Response("Some Get Response")

