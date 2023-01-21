from .models import Order, OrderList
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer, OrderListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the order list to be viewed or edited.
    """
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [permissions.AllowAny]
