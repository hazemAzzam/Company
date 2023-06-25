from rest_framework.viewsets import ModelViewSet
from project_app.serializers import *

class Project_View(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=Project_Serializer

class Employee_Works_On_Project_View(ModelViewSet):
    queryset=Employee_Works_On_Project.objects.all()
    serializer_class=Employee_Works_On_Project_Serializer

class Department_Controls_Projects_View(ModelViewSet):
    queryset=Department_Controls_Projects.objects.all()
    serializer_class=Department_Controls_Projects_Serializer