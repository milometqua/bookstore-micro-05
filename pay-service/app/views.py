from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment


@api_view(['POST'])
def pay(request):

    order_id = request.data.get("order_id")

    payment = Payment.objects.create(
        order_id=order_id,
        status="success"
    )

    return Response({
        "payment_id": payment.id,
        "status": payment.status
    })