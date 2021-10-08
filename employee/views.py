
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from employee.form import EmployeeForm
from employee.models import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "index.html", {"form": form})


def show(request):
    emp = Employee.objects.all()
    return render(request, "show.html", {"emp": emp})



def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("/")


def update(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'emp': emp})


def base(request):
    return HttpResponse("<h1> Hello ,Django !!</h1>")