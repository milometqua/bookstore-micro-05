from django.contrib import admin
from django.urls import path
from views import books_api, books, book_detail, register_customer, login_customer, logout_customer, manage_books, add_book, edit_book, delete_book, view_cart, add_to_cart, checkout, rate_book, update_cart_item, delete_cart_item   # vì views.py nằm ngoài

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', books_api),
    path('api/cart/item/<int:item_id>/', update_cart_item),
    path('api/cart/item/<int:item_id>/delete/', delete_cart_item),
    path('books/', books, name='books'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('register/', register_customer, name='register'),
    path('login/', login_customer, name='login'),
    path('logout/', logout_customer, name='logout'),
    path('manage-books/', manage_books, name='manage_books'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('cart/<int:customer_id>/', view_cart, name='view_cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('rate-book/<int:book_id>/', rate_book, name='rate_book'),
]