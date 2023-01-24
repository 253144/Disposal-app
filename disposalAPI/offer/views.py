from .models import Container, Price
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContainerSerializer, PriceSerializer


class ContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Containers to be viewed or edited.
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticated]

class PriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prices to be viewed or edited.
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [permissions.IsAuthenticated]
