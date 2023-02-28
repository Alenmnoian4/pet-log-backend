from .models import Petlog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our Serializer
class PetlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Petlog
        # the fields that should be included in the serialized output
        fields = ['id', 'pet', 'date', 'weight', 'appointments', 'notes']