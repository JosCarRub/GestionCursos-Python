from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Estudiante, Inscripcion
from .forms import CursoForm, EstudianteForm, InscripcionForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class ListarCursos(ListView):
    model = Curso
    template_name= 'app/listar_cursos.html'
    context_object_name = 'cursos'

class CrearCurso(CreateView):
    model = Curso
    template_name = 'app/crear_curso.html'
    form_class = CursoForm
    success_url = reverse_lazy('listar_cursos')



def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'app/listar_cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'app/crear_curso.html', {'form': form})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'app/editar_curso.html', {'form': form})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'app/confirmar_eliminacion.html', {'objeto': curso})



def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'app/listar_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'app/crear_estudiante.html', {'form': form})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'app/editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'app/confirmar_eliminacion.html', {'objeto': estudiante})



def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'app/listar_inscripciones.html', {'inscripciones': inscripciones})

def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'app/crear_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'app/confirmar_eliminacion.html', {'objeto': inscripcion})
