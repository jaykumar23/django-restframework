from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello(request):
#     return Response({'msg': 'Hello'})

# @api_view(['GET'])
# def hello(request):
#     return Response({'msg': 'Hello'})

@api_view(['POST','GET'])
def hello(request):
    if request.method == "GET":
        print(request.data)
        return Response({'msg': 'Hello get request'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'Hello post request', 'data': request.data})