"""
URL configuration for tegoWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from tegoWebsite import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('admin/', admin.site.urls),
    path('encode/', views.encode_audio_view, name='encode'),
    path('decode/', views.decode_audio_view, name='decode'),
    path('encode_video/', views.encode_video_view, name='encode_video'),
    path('decode_video/', views.decode_video_view, name='decode_video'),
    path('encode_image/', views.encode_image_view, name='encode_image'),
    path('decode_image/', views.decode_image_view, name='decode_image'),
    path('decode_remake/', views.decode_audio_remake_view, name='decode_remake'),
    path('encode_remake/', views.encode_audio_remake_view, name='encode_remake'),
    path('decode_video_remake/', views.decode_video_remake_view, name='decode_video_remake'),
    path('encode_video_remake/', views.encode_video_remake_view, name='encode_video_remake'),
    path('decode_image_remake/', views.decode_image_remake_view, name='decode_image_remake'),
    path('encode_image_remake/', views.encode_image_remake_view, name='encode_image_remake'),
]
