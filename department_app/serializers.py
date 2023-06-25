from rest_framework.customs import ComplexSerializer, SlugRelatedField, ModelSerializer, StringRelatedField, ListField
from .models import Department, Employee_Manager
from project_app.serializers import Department_Controls_Projects_Serializer

class Department_Serializer(ComplexSerializer):
    #controls = Department_Controls_Projects_Serializer(read_only=True, exclude=['department'], many=True)
    #controls = StringRelatedField(source='controls.first')
    controls = SlugRelatedField(slug_field='project_name', read_only=True, many=True)   
    class Meta:
        model=Department
        fields="__all__"