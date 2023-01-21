from .models import Contener, Price
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContenerSerializer, PriceSerializer


class ContenerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conteners to be viewed or edited.
    """
    queryset = Contener.objects.all()
    serializer_class = ContenerSerializer
    permission_classes = [permissions.AllowAny]

class PriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prices to be viewed or edited.
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [permissions.AllowAny]
