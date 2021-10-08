from django.contrib import admin
from django.urls import path

from employee.views import base, emp, show, delete, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', emp),
    path('', show),
    path('delete/<int:id>/', delete),
    path('update/<int:id>/', update),
    path('base/',base),
]
