from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Employee_View(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employee_Serializer

class Dependent_View(ModelViewSet):
    queryset=Dependent.objects.all()
    serializer_class=Dependent_Serializer