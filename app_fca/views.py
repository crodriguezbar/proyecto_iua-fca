from django.shortcuts import render
from app_fca.models import Docentes

# Create your views here.

def inicio (request):
    return render(request, 'plantillas/home.html')

def alta_docente (request):
    return render(request, 'formularios/docentes/form_alta_docente.html')

def form_alta_docente (request):
    if request.method == 'POST':
        f_alta_docente=FormAltaDocente (request.POST)
        
        if f_alta_docente.is_valid():
            data = f_alta_docente.cleaned_data
            alta_docente1=alta_docente(nombre=data.get('nombre'), apellido=data.get('apellido'), dni=data.get('dni'), titulo_grado=data.get('titulo_grado'), hs_asignar=data.get('hs_asignar'), metodo_alta=data.get('metodo_alta'), fecha_alta=data.get('fecha_alta'))
            alta_docente1.saved()    
        else: 
            pass #falta completar
        
    return render(request, 'formularios/docentes/form_alta_docente.html')