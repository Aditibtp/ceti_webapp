from django.shortcuts import render

def home(request):

    if request.user.username:
        return render(request, 'pages/home.html')
    else:
        return render(request, 'accounts/login.html')


def about(request):
    return render(request, 'pages/about.html')

