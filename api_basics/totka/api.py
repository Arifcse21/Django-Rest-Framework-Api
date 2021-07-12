from totka.models import Info
from rest_framework import viewsets, permissions
from .serializers import InfoSerializer


# Info viewset
class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InfoSerializer