from django.db import models

# Create your models here.
class Employee(models.Model):
    ssn = models.CharField(max_length=15, primary_key=True)
    birth_date = models.DateField()
    fname = models.CharField(max_length=50, null=False, blank=False)
    minit = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)

    @property
    def name(self):
        return f"{self.fname} {self.minit} {self.lname}"
    
    address = models.CharField(max_length=150, null=True, blank=True)
    salary = models.PositiveBigIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=12, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ], null=True, blank=True)

    supervisor = models.OneToOneField("Employee", on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def supervisee(self):
        return Employee.objects.filter(supervisor=self)
    
    works_for = models.ForeignKey("department_app.Department", related_name='employees', on_delete=models.SET_NULL, null=True)

class Dependent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='dependents')
    name = models.CharField(max_length=150)
    sex = models.CharField(max_length=12, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ], null=True, blank=True)
    birth_date = models.DateField()
    relaationship = models.CharField(max_length=50)
