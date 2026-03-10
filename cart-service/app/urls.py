from django.urls import path
from .views import AddCartItem, ViewCart, CartCreate, UpdateCartItem, DeleteCartItem

urlpatterns = [
    path("cart/create/", CartCreate.as_view()),
    path("cart/add/", AddCartItem.as_view()),
    path("cart/<int:customer_id>/", ViewCart.as_view()),
    path("cart/item/<int:item_id>/", UpdateCartItem.as_view()),
    path("cart/item/<int:item_id>/delete/", DeleteCartItem.as_view()),
]