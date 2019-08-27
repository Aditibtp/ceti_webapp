from rest_framework import generics
from .serializers import StorageSerializer
from .models import Storage
from rest_framework import permissions
from .permissions import IsOwner

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Storage.objects.all()

    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        """Save the post data when creating a new storage id."""

        serializer.save(user_id=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

