from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def recommend(request, customer_id):

    return Response([
        {"book_id": 1},
        {"book_id": 2},
        {"book_id": 3}
    ])