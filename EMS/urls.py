from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, employee_dashboard

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', employee_dashboard, name='employee_dashboard'),
    path('api/', include(router.urls)),
]
