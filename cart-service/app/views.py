from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
import requests

BOOK_SERVICE_URL = "http://book-service:8000"


class CartCreate(APIView):

    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCartItem(APIView):

    def post(self, request):

        book_id = request.data.get("book_id")
        customer_id = request.data.get("customer_id")
        cart_id = request.data.get("cart")
        quantity = request.data.get("quantity", 1)

        # Hỗ trợ cả customer_id và cart_id
        if not book_id:
            return Response({"error": "book_id is required"}, status=400)
        
        if not customer_id and not cart_id:
            return Response({"error": "Either customer_id or cart_id is required"}, status=400)

        # Nếu có customer_id, tìm cart từ customer_id
        if customer_id and not cart_id:
            try:
                cart = Cart.objects.get(customer_id=customer_id)
                cart_id = cart.id
            except Cart.DoesNotExist:
                return Response({"error": "Cart not found for this customer"}, status=404)

        # gọi book-service
        try:
            r = requests.get(f"{BOOK_SERVICE_URL}/books/")
            if r.status_code != 200:
                return Response({"error": "Book service unavailable"}, status=500)

            books = r.json()

        except Exception as e:
            return Response({"error": "Book service error"}, status=500)

        # kiểm tra book tồn tại
        if not any(b["id"] == book_id for b in books):
            return Response({"error": "Book not found"}, status=404)

        # Kiểm tra xem item đã tồn tại chưa
        try:
            existing_item = CartItem.objects.get(cart_id=cart_id, book_id=book_id)
            existing_item.quantity += quantity
            existing_item.save()
            serializer = CartItemSerializer(existing_item)
            return Response(serializer.data, status=200)
        except CartItem.DoesNotExist:
            # Tạo CartItem mới
            try:
                cart_item = CartItem.objects.create(
                    cart_id=cart_id,
                    book_id=book_id,
                    quantity=quantity
                )
                serializer = CartItemSerializer(cart_item)
                return Response(serializer.data, status=201)
            except Exception as e:
                return Response({"error": str(e)}, status=400)


class ViewCart(APIView):

    def get(self, request, customer_id):

        try:
            cart = Cart.objects.get(customer_id=customer_id)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=404)

        items = CartItem.objects.filter(cart=cart)

        serializer = CartItemSerializer(items, many=True)

        return Response(serializer.data)


class UpdateCartItem(APIView):

    def put(self, request, item_id):
        try:
            cart_item = CartItem.objects.get(id=item_id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=404)

        quantity = request.data.get("quantity")
        if quantity is not None:
            if quantity <= 0:
                cart_item.delete()
                return Response({"message": "Item removed"}, status=200)
            cart_item.quantity = quantity
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=200)
        else:
            return Response({"error": "Quantity is required"}, status=400)


class DeleteCartItem(APIView):

    def delete(self, request, item_id):
        try:
            cart_item = CartItem.objects.get(id=item_id)
            cart_item.delete()
            return Response({"message": "Item removed"}, status=200)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=404)