from django.urls import path
from . import views

urlpatterns = [
    path('app/cursos/', views.listar_cursos, name='listar_cursos'),
    path('app/cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),

    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),

    path('inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('inscripciones/crear/', views.crear_inscripcion, name='crear_inscripcion'),
]