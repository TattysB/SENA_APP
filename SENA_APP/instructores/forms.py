from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            "tipo_documento",
            "documento_id",
            "nombre",
            "apellido",
            "telefono",
            "correo",
            "fecha_nacimiento",
            "ciudad",
            "direccion",
            "nivel_educativo",
            "especialidad",
            "anos_experiencia",
            "activo",
            "fecha_vinculacion",
        ]
        widgets = {
            "tipo_documento": forms.Select(attrs={"class": "form-select"}),
            "documento_id": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Número de documento"}
            ),
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Teléfono"}
            ),
            "correo": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "correo@ejemplo.com"}
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "ciudad": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ciudad"}
            ),
            "direccion": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "placeholder": "Dirección"}
            ),
            "nivel_educativo": forms.Select(attrs={"class": "form-select"}),
            "especialidad": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Especialidad"}
            ),
            "anos_experiencia": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Años"}
            ),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "fecha_vinculacion": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
