from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
# Model object - Single Student Data

def student_detail(request, pk):
    stu = Students.objects.get(id=pk)
    serializer = StudentsSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# Query Set

def student_info(request):
    stu = Students.objects.all()
    serializer = StudentsSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
