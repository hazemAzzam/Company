from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    location = models.CharField(max_length=150, null=True, blank=True)


    def __str__(self):
        return f"{self.name}"
    
class Employee_Works_On_Project(models.Model):
    employee = models.ForeignKey("employee_app.Employee", on_delete=models.CASCADE, related_name='works_on')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='employees')

    hours = models.IntegerField()

class Department_Controls_Projects(models.Model):
    department = models.ForeignKey("department_app.Department", on_delete=models.CASCADE, related_name='controls')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='controled_by')

    class Meta:
        unique_together = ('department', 'project')
    @property
    def project_name(self):
        return f"{self.project.name}"
    
    def __str__(self):
        return f"{self.project}"
    