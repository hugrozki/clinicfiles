from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .serializers import RecordSerializer

@api_view(['GET'])
def accounts_list(request, pk, format=None):
    try:
        record = Account.objects.get(pk=pk)
    except Account.DoesNotExist as e:
        data = {
            "codigo": 400,
            "mensaje" : "El id de usuario no existe",
        }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=RecordSerializer(record)

        data = {
         "codigo": 200,
         "mensaje": "Petición completada",
         "payload" : serializer.data
        }

        return Response(data)
