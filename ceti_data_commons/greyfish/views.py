from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UploadFileForm
from greyfish_py import greyfish
import os


# Helper function for upload view
def handle_uploaded_file(f, g_id):
    path = os.path.join(settings.BASE_DIR, 'upload/test/test.txt')
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # Upload to Greyfish - check for g_id beforehand?
    # greyfish.upload_file(g_id, path)


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.userprofile
            handle_uploaded_file(request.FILES['file'], profile.g_id)
            return HttpResponseRedirect(reverse('upload_success'))
    else:
        form = UploadFileForm()
    return render(request, 'greyfish/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'greyfish/upload_success.html')
