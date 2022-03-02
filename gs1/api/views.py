import json
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    s = StudentSerializer(stu)
    #j = JSONRenderer().render(s.data)
    #return HttpResponse(j, content_type='application/json')
    return JsonResponse(s.data)

def students_detail(request):
    stu = Student.objects.all()
    s = StudentSerializer(stu,many=True)
    #j = JSONRenderer().render(s.data)
    #return HttpResponse(j, content_type='application/json')
    return JsonResponse(s.data, safe=False)