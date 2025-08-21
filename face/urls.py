from django.urls import path

from .views import members

urlpatterns = [
    path('v1/', members),
]