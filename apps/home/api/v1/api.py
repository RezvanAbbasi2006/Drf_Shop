from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.home.serializers import HomeSerializer
from apps.product.models import Product


class HomeAPI(APIView):

    def get(self):
        pass