from rest_framework import serializers
from .models import CetiJobs

class CetiJobsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    user_id = serializers.ReadOnlyField(source='user_id.id')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CetiJobs
        fields = ('user_id','created_at', 'job_title', 'status', 'node','gpu','latest_run', 'finished_at', 'script_file', 'dir_used')
        read_only_fields = ['created_at',]