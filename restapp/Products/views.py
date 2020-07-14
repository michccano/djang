from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)

