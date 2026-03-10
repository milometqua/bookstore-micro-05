from django.urls import path
from .views import ship

urlpatterns = [
    path('ship/', ship),
]