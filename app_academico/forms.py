from django import forms
from .models import Docente, Alumno

class FormAlumno(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Alumno
        fields = ('foto',)

class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Docente
        fields = ('foto',)



