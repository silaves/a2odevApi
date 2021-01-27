from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProblemSerializer
from .problems import Problems



@api_view(['POST'])
def problem_1(request):
    obj = ProblemSerializer(data = request.data)
    
    if not obj.is_valid():
        error_list = [obj.errors[error][0] for error in obj.errors]
        return Response(error_list,status=status.HTTP_400_BAD_REQUEST)
        
    try:
        solution = Problems.problemA(obj.validated_data['input_data'])
        if solution == '':
            return Response({'Error al cargar los datos, verifique los datos de entrada'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Error al cargar los datos, verifique los datos de entrada'},status=status.HTTP_400_BAD_REQUESTR)

    return Response({'data':solution}, status=status.HTTP_200_OK)


@api_view(['POST'])
def problem_2(request):
    obj = ProblemSerializer(data = request.data)

    if not obj.is_valid():
        error_list = [obj.errors[error][0] for error in obj.errors]
        return Response(error_list,status=status.HTTP_400_BAD_REQUEST)

    try:
        solution = Problems.problemB(obj.validated_data['input_data'])
    except Exception as e:
        return Response({'Error al cargar los datos, verifique los datos de entrada'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'data':solution}, status=status.HTTP_200_OK)


@api_view(['POST'])
def problem_3(request):
    obj = ProblemSerializer(data = request.data)
    
    if not obj.is_valid():
        error_list = [obj.errors[error][0] for error in obj.errors]
        return Response(error_list,status=status.HTTP_400_BAD_REQUEST)

    try:
        solution = Problems.problemC(obj.validated_data['input_data'])
    except Exception as e:
        return Response({'Error al cargar los datos, verifique los datos de entrada'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'data':solution}, status=status.HTTP_200_OK)