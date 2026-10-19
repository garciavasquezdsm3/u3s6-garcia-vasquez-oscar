# path: función para declarar una ruta URL y a qué vista apunta
from django.urls import path
# views: el módulo con todas las funciones-vista de esta app
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
