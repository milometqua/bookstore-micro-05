from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
import requests

CART_SERVICE_URL = "http://cart-service:8000"

class CustomerListCreate(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            customer = serializer.save()

            # gọi cart service
            requests.post(
                f"{CART_SERVICE_URL}/cart/create/",
                json={"customer_id": customer.id}
            )

            return Response(serializer.data)

        return Response(serializer.errors)


class CustomerCheck(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        
        if not email or not password:
            return Response({'error': 'Email and password required'}, status=400)
        
        try:
            customer = Customer.objects.get(email=email, password=password)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=404)