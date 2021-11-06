from django import forms

from .models import Department, Rank, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name", "description")
        lables = {
            "name": "Название отдела",
            "description": "Описание отдела",
        }


class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ("name", "description")
        lables = {
            "name": "Название должности",
            "description": "Описание должности",
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "year_in_school",
            "dob",
            "department",
            "rank",
            "date_accepted",
            "years_worked",
        )
        lables = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "middle_name": "Отчество",
            "year_in_school": "Образование",
            "dob": "Дата рождения",
            "department": "Отдел",
            "rank": "Должность",
            "date_accepted": "Дата принятия на работу",
            "years_worked": "Стаж",
        }
