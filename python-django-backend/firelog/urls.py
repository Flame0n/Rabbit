"""firelog URL Configuration

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
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign_in, name='sign_in'),
    path('dashboard/', views.post_sign, name='post_sign'),
    path('logout/', views.logout, name='logout'),
    path('password/reset/', views.password_reset_view, name='password_reset'),
    path('password/reset/sent/', views.password_reset_sent, name='password_reset_sent'),
    path('signup/', views.signup, name='signup'),
    path('callback/', views.callback, name='callback'),
    path('order/', views.order, name='order'),
]
