from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            "codigo",
            "nombre",
            "programa",
            "instructor_coordinador",
            "fecha_inicio",
            "fecha_fin",
            "horario",
            "aula",
            "cupos_maximos",
            "estado",
            "observaciones",
        ]
        widgets = {
            "codigo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: CRS001"}
            ),
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del curso"}
            ),
            "programa": forms.Select(attrs={"class": "form-select"}),
            "instructor_coordinador": forms.Select(attrs={"class": "form-select"}),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "horario": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 8:00 AM - 5:00 PM"}
            ),
            "aula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Aula 101"}
            ),
            "cupos_maximos": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "30"}
            ),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Observaciones...",
                }
            ),
        }
