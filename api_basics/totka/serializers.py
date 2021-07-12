from rest_framework import serializers
from totka.models import Info

# Load Serializer
class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'