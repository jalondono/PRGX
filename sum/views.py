from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Operation
from .serializers import OperationSerializer


def validate_number(a, b):
    """Validate if a is a number is None"""
    if a is None:
        a = 0
    if b is None:
        b = 0
    return a, b


@api_view(['GET', 'POST'])
def operation_body(request):
    """List all operations , or create a new operation From body request"""
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        a = float(request.data.get('number_1'))
        b = float(request.data.get('number_2'))
        a, b = validate_number(a, b)
        request.data['result'] = str(a + b)

        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def operation_url(request):
    """
    Create a  new operation from a query string.
    """
    if request.method == 'POST':
        a = float(request.query_params.get('num1'))
        b = float(request.query_params.get('num2'))
        a, b = validate_number(a, b)
        c = a + b
        data_process = {'number_1': str(a),
                        'number_2': str(b),
                        'result': str(c)}
        serializer = OperationSerializer(data=data_process)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
