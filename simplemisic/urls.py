"""simplemisic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app01 import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login,name='login'),

    path('index/',views.index,name='index'),

    path('register/',views.register,name='register'),

    path('my_music/',views.my_music,name='my_music'),

    path('music_hall/',views.music_hall,name='music_hall'),

    path('about/',views.about,name='about'),

    path('user/',views.info_lisrt,name='userinfo'),

    path('user/delete/',views.delete,name='userdelete'),

    path('imagco/',views.img_code),

    path('loginout/',views.loginout),

    path('search/',views.music_search,name='search')
]
