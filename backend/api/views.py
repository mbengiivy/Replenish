from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def products_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def orders_list(request):
    queryset = Order.objects.all()
    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def staff_count(request):
    count = User.objects.filter(is_staff=True).count()
    return Response({'count': count})