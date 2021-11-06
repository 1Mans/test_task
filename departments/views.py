from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Department, Employee, Rank
from .forms import DepartmentForm, RankForm, EmployeeForm


@login_required
def index(request):
    employees = Employee.objects.all()
    return render(request, "departments/index.html", {"employees": employees})


@login_required
def rank_list(request):
    ranks = Rank.objects.all()
    return render(request, "departments/rank.html", {"ranks": ranks})


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, "departments/departments.html", {"departments": departments})


@login_required
def new_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
        return render(request, "departments/new.html", {"form": form})
    form = DepartmentForm()
    return render(request, "departments/new.html", {"form": form})


@login_required
def new_rank(request):
    if request.method == "POST":
        form = RankForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
        return render(request, "departments/new_rank.html", {"form": form})
    form = RankForm()
    return render(request, "departments/new_rank.html", {"form": form})


@login_required
def new_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
        return render(request, "departments/new_employee.html", {"form": form})
    form = EmployeeForm()
    return render(request, "departments/new_employee.html", {"form": form})


@login_required
def employee_edit(request, employee):
    employee_id = get_object_or_404(Employee, id=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee_id)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(
            request,
            "departments/new_employee.html",
            {"form": form, "employee": employee_id},
        )
    form = EmployeeForm()
    return render(
        request,
        "departments/new_employee.html",
        {"form": form, "employee": employee_id},
    )


@login_required
def rank_edit(request, rank):
    rank_id = get_object_or_404(Rank, id=rank)
    if request.method == "POST":
        form = RankForm(request.POST, instance=rank_id)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(
            request,
            "departments/new_rank.html",
            {"form": form, "rank": rank_id},
        )
    form = RankForm()
    return render(
        request,
        "departments/new_rank.html",
        {"form": form, "rank": rank_id},
    )


@login_required
def department_edit(request, department):
    department_id = get_object_or_404(Department, id=department)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department_id)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(
            request,
            "departments/new.html",
            {"form": form, "department": department_id},
        )
    form = DepartmentForm()
    return render(
        request,
        "departments/new.html",
        {"form": form, "department": department_id},
    )


@login_required
def department_delete(request, department):
    department_id = get_object_or_404(Department, id=department)
    department_id.delete()
    return redirect("/")


@login_required
def employee_delete(request, employee):
    employee_id = get_object_or_404(Employee, id=employee)
    employee_id.delete()
    return redirect("/")
