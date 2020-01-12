from rest_framework import serializers
from .models import CetiJobs

class CetiJobsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    user_id = serializers.ReadOnlyField(source='user_id.id')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CetiJobs
        fields = ('created_at', 'job_title', 'status', 'dir_used', 'script_file')
        read_only_fields = ['created_at',]