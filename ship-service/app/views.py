from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shipment


@api_view(['POST'])
def ship(request):

    order_id = request.data.get("order_id")
    address = request.data.get("address")

    shipment = Shipment.objects.create(
        order_id=order_id,
        address=address
    )

    return Response({
        "shipment_id": shipment.id,
        "status": "shipping_created"
    })