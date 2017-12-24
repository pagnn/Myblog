"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from rest_framework_jwt.views import obtain_jwt_token

from .views import homeView,contactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('contact/',contactView,name='contact'),
    path('posts/', include('posts.urls',namespace='posts')),
    path('comments/', include('comments.urls',namespace='comments')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('api/auth/token', obtain_jwt_token),
    path('api/posts/', include('posts.api.urls',namespace='posts-api')),
    path('api/comments/', include('comments.api.urls',namespace='comments-api')),
    path('api/accounts/', include('accounts.api.urls',namespace='accounts-api')),

]
if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
