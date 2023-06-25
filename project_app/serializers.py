from rest_framework.customs import ComplexSerializer, CharField, StringRelatedField, ModelSerializer
from .models import *

class Department_Controls_Projects_Serializer(ComplexSerializer):
    department=StringRelatedField()
    project=StringRelatedField()
    class Meta:
        model=Department_Controls_Projects
        fields="__all__"

class Employee_Works_On_Project_Serializer(ComplexSerializer):
    name = CharField(source='project.name', read_only=True)
    class Meta:
        model=Employee_Works_On_Project
        fields=['id', 'employee', 'name', 'hours']

class Project_Serializer(ComplexSerializer):
    class Meta:
        model=Project
        fields="__all__"