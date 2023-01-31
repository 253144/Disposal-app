from .models import Order, OrderList
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderDetailSerializer, OrderDefaultSerializer, OrderListDetailSerializer, OrderListDefaultSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderDefaultSerializer
        return OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the order list to be viewed or edited.
    """
    queryset = OrderList.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderListDefaultSerializer
        return OrderListDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
