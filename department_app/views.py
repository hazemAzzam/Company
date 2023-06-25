from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Department_View(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=Department_Serializer