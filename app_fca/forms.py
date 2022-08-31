from django import forms

class FormAltaDocente (forms.Form):
    nombre=forms.CharField(max_length=40, required=True)
    apellido=forms.CharField(max_length=40, required=True)
    dni=forms.IntegerField(required=True)
    titulo_grado=forms.CharField(max_length=40, required=True)
    titulo_posgrado=forms.CharField(max_length=40)
    hs_asignar=forms.IntegerField(required=True)
    metodo_alta=forms.CharField(max_length=100, required=True)
    fecha_alta=forms.DateField(required=True)   