from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    location = models.TextField
    
    @property
    def number_of_employee(self):
        return self.employees
    
    class Meta:
        unique_together = ('name', 'number')

    def __str__(self):
        return f"{self.name}"


class Employee_Manager(models.Model):
    employee = models.ForeignKey("employee_app.Employee", on_delete=models.CASCADE, related_name='manages', unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='manager', unique=True)
    since = models.DateField(auto_now_add=True)