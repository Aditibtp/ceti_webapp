"""ceti_data_commons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from pages import views as pages_views
from accounts import views as accounts_views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages_views.home, name='home'),
    path('about/', pages_views.about, name='about'),
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('dashboard/', accounts_views.dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('datacommons/', include('greyfish.urls')),
    url(r'^', include('generate_g_id.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
