from functools import partial
import imp
import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from.models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def std_api(request):
    if request.method == "GET":
        js_data = request.body
        stream = io.BytesIO(js_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            js_data = JSONRenderer().render(serializer.data)
            return HttpResponse(js_data, content_type="application/json")
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        js_data = JSONRenderer().render(serializer.data)
        return HttpResponse(js_data, content_type="application/json")
    
    if request.method == "POST":
        js_data = request.body
        stream = io.BytesIO(js_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted'}
            js_data = JSONRenderer().render(res)
            return HttpResponse(js_data, content_type="application/json")
        else:
            js_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(js_data, content_type="application/json")
        
    if request.method == "PUT":
        js_data = request.body
        stream = io.BytesIO(js_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id=id)

        #partial update
        #serializer = StudentSerializer(stu,data=py_data, partial=True)

        # update
        serializer = StudentSerializer(stu,data=py_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data upadted partially'}
            # js_data = JSONRenderer().render(res)
            # return HttpResponse(js_data, content_type="application/json")
            return JsonResponse(res, safe=False)

        else:
            # js_data = JSONRenderer().render(serializer.errors)
            # return HttpResponse(js_data, content_type="application/json")
            return JsonResponse(serializer.errors, safe=False)

    if request.method == "DELETE":
        js_data = request.body
        stream = io.BytesIO(js_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data deleted '}
        # js_data = JSONRenderer().render(res)
        # return HttpResponse(js_data, content_type="application/json")
        return JsonResponse(res, safe=False)
    