from django.contrib import admin

from employee.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','ename','eemail','econtact')
    search_fields=('ename',)
    list_per_page=5
admin.site.register(Employee,EmployeeAdmin)