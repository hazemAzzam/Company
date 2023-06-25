from rest_framework.customs import ComplexSerializer, SerializerMethodField, SlugRelatedField, PrimaryKeyRelatedField
from .models import *
from project_app.serializers import Employee_Works_On_Project_Serializer


class Dependent_Serializer(ComplexSerializer):
    employee = PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=False)
    class Meta:
        model = Dependent
        fields="__all__"

class Employee_Serializer(ComplexSerializer):
    supervisee = SlugRelatedField(slug_field='ssn', read_only=True, many=True)
    works_for = SlugRelatedField(slug_field='name', read_only=True)
    works_on = Employee_Works_On_Project_Serializer(many=True, read_only=True, exclude=['employee', 'id'])
    dependents = Dependent_Serializer(exclude=['employee'], many=True, forign_key='employee')
    class Meta:
        model=Employee
        fields=['ssn', 'name', 'fname', 'minit', 'lname', 'birth_date','sex', 'works_for', 'supervisor', 'supervisee', 'works_on', 'dependents']

