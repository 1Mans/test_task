from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rank/", views.rank_list, name="rank_list"),
    path("department/", views.department_list, name="department_list"),
    path("new/department", views.new_department, name="new_department"),
    path("new/rank", views.new_rank, name="new_rank"),
    path("new/employee", views.new_employee, name="new_employee"),
    path("<int:employee>/edit/", views.employee_edit, name="employee_edit"),
    path(
        "<int:department>/department/edit/",
        views.department_edit,
        name="department_edit",
    ),
    path("<int:rank>/rank/edit/", views.rank_edit, name="rank_edit"),
    path(
        "<int:department>/department/delete/",
        views.department_delete,
        name="department_delete",
    ),
    path(
        "<int:employee>/employee/delete/", views.employee_delete, name="employee_delete"
    ),
]
