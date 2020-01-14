from django.shortcuts import render
from rest_framework import generics
from .serializers import CetiJobsSerializer
from .models import CetiJobs

# Create your views here.
def create_job(request):
    hpcjobs = CetiJobs.objects.order_by('-created_at').filter(user_id=request.user)
    context = {
        'hpcjobs': hpcjobs
    }
    return render(request, 'jobs/job_home.html', context)

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""

    serializer_class = CetiJobsSerializer

    def get_queryset(self):
        return CetiJobs.objects.all().filter(user_id=self.request.user)

    def perform_create(self, serializer):
        """Save the post data when creating a new job."""
        print("came till here")
        serializer.save(user_id=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
    queryset = CetiJobs.objects.all()
    serializer_class = CetiJobsSerializer