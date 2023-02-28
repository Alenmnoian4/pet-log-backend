from .models import Petlog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PetlogSerializer


class PetlogViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Petlog.objects.all()
    # The serializer class for serializing output
    serializer_class = PetlogSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]