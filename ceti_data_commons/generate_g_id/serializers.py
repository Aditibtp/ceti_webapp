from rest_framework import serializers
from .models import Storage

class StorageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    user_id = serializers.ReadOnlyField(source='user_id.id')  # ADD THIS LINE
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Storage
        fields = ('storage_id', 'user_id', 'created_at')
        read_only_fields = ['created_at']