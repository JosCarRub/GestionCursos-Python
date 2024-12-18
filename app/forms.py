from datetime import date, timedelta
from django import forms
from .models import Curso, Estudiante, Inscripcion


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin']
        widgets = {'fecha_inicio': forms.DateInput (format='%Y-%m-%d', attrs={'type':'date'}),
                   'fecha_fin': forms.DateInput (format='%Y-%m-%d', attrs={'type':'date'})}
            

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise forms.ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'fecha_nacimiento']
        widgets = {'fecha_nacimiento': forms.DateInput (format='%Y-%m-%d', attrs={'type':'date'})}

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento > date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede ser posterior al día actual.")
        if fecha_nacimiento > date.today() - timedelta(days=18 * 365):
            raise forms.ValidationError("El estudiante debe tener al menos 18 años.")
        return fecha_nacimiento


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']
        widgets = {'fecha_inscripcion': forms.DateInput (format='%Y-%m-%d', attrs={'type':'date'})}


    def clean(self):
        cleaned_data = super().clean()
        curso = cleaned_data.get('curso')
        fecha_inscripcion = cleaned_data.get('fecha_inscripcion')

        if curso and fecha_inscripcion:
            if curso.fecha_fin < fecha_inscripcion:
                raise forms.ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        return cleaned_data