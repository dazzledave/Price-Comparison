# urls.py (inside your app directory)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
