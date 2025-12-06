from django import forms
from .models import Aprendiz


class AprendizForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar aprendices"""
    
    class Meta:
        model = Aprendiz
        fields = [
            'document_id',
            'firstname',
            'lastname',
            'phone',
            'email',
            'birthdate',
            'city'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'document_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            })
        }
        # Etiquetas personalizadas
        labels = {
            'document_id': 'Documento de Identidad',
            'firstname': 'Nombre',
            'lastname': 'Apellido',
            'phone': 'Teléfono',
            'email': 'Correo Electrónico',
            'birthdate': 'Fecha de Nacimiento',
            'city': 'Ciudad'
        }

    # Validaciones personalizadas
    
    def clean_document_id(self):
        """Validar que el documento contenga solo números"""
        documento = self.cleaned_data.get('document_id')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_phone(self):
        """Validar que el teléfono contenga solo números"""
        telefono = self.cleaned_data.get('phone')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono