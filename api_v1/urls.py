from rest_framework.routers import DefaultRouter
from employee_app.views import *
from department_app.views import *
from project_app.views import *
from django.urls import path, include

router = DefaultRouter()

router.register('employees', Employee_View)

router.register('departments', Department_View)

router.register('projects', Project_View)
router.register('works_on', Employee_Works_On_Project_View)
router.register('controls', Department_Controls_Projects_View)

router.register('dependents', Dependent_View)

urlpatterns = [
    path('', include(router.urls))
]
