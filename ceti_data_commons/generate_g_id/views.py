from rest_framework import generics
from .serializers import StorageSerializer
from .models import Storage


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""

    serializer_class = StorageSerializer

    def get_queryset(self):
        return Storage.objects.all().filter(user_id=self.request.user)

    def perform_create(self, serializer):
        """Save the post data when creating a new storage id."""
        serializer.save(user_id=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer