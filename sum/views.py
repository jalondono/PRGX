from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Operation
from .serializers import OperationSerializer


@api_view(['GET', 'POST'])
def operation_body(request):
    """List all operations , or create a new operation."""
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        a = float(request.data['number_1'])
        b = float(request.data['number_2'])
        request.data['result'] = str(a + b)
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
