from django.urls import path
from .views import CustomerListCreate, CustomerCheck

urlpatterns = [
    path('customers/', CustomerListCreate.as_view()),
    path('customers/check/', CustomerCheck.as_view()),
]