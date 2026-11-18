"""
URL configuration for vocalbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.maintenance, name='M'),
    path('dlsu_ccinfom/', admin.site.urls),

    # # Concert Model
    # path('concerts/', views.concert, name='C'),
    # path('concerts/modify', views.update_concert, name='UC'),
    # path('concerts/remove', views.delete_concert, name='DC'),
    #
    # Producer Model
    path('producers/', views.producers, name='P'),
    path('producers/modify', views.update_producer, name='UP'),
    path('producers/remove', views.delete_producer, name='DP'),
    #
    # # Song Model
    # path('songs/', views.song, name='S'),
    # path('songs/modify', views.update_song, name='US'),
    # path('songs/remove', views.delete_song, name='DS'),
    #
    # # Setlist Model
    # path('setlist/', views.setlist, name='CS'),
    # path('setlist/modify', views.update_setlist, name='UCS'),
    # path('setlist/remove', views.delete_setlist, name='DCS'),

    # VOCALOID Model
    path('vocaloid/', views.vocaloid, name='V'),
    path('vocaloid/modify', views.update_vocaloid, name='UV'),
    path('vocaloid/remove', views.delete_vocaloid, name='DV')
]